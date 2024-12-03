from django.shortcuts import render, redirect, get_object_or_404
from .models import Contrato, Supervisor, Contratista, Rol, MODALIDAD_SELECCION_CHOICES
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ContratoForm, SupervisorForm, ContratistaForm
from django.http import HttpResponse
import csv
import json
from django.utils import timezone
from datetime import date
from django.core.mail import send_mail
from django.db.models import Q
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# ---------------------------- RENDER ----------------------------
# Estas vistas realizan procesos que terminan en un render, es decir,
# generan una respuesta visual para el usuario. Su propósito es mostrar
# información al usuario de manera clara y dinámica.
# -----------------------------------------------------------------------

# contrato ---------------------------------------------------------------------------------------------------------------------    
@login_required
def crear_contrato(request):
    rol = Rol.objects.all()
    supervisor = Supervisor.objects.all()
    contratista = Contratista.objects.all()
    usuarios = User.objects.all()
    if request.method == 'POST':
        form = ContratoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'El contrato ha sido creado con éxito.')
            return redirect('contrato')  # Redirige a la misma página o a donde desees
        else:
            messages.error(request, 'Hubo un error al crear el contrato. Verifica los campos.')
            print(form.errors)  # Imprimir errores para depuración
    else:
        form = ContratoForm()

    context = {
        'form': form,
        'supervisor': supervisor,
        'contratista': contratista,
        'rol': rol,
        'usuarios': usuarios,
    }
    
    return render(request, 'contract/create_contract.html', context)

@login_required
def contratosview(request):

    contratos = Contrato.objects.all().order_by('-id')  # Ordenamos por ID de forma descendente

    hoy = date.today()

    # Cálculo de días restantes
    for contrato in contratos:
        if contrato.plazo_fin:
            contrato.dias_restantes = (contrato.plazo_fin - hoy).days
        else:
            contrato.dias_restantes = None

    # Búsqueda
    search_query = request.GET.get('search')
    if search_query:
        contratos = contratos.filter(
            Q(numero_contrato__icontains=search_query) |
            Q(objeto__icontains=search_query)
        )

    # Filtros
    supervisor = request.GET.get('supervisor')
    if supervisor:
        contratos = contratos.filter(supervisor__id=supervisor)

    contratista = request.GET.get('contratista')
    if contratista:
        contratos = contratos.filter(contratista__id=contratista)

    usuario_asociado = request.GET.get('usuario_asociado')
    if usuario_asociado:
        contratos = contratos.filter(
            Q(supervisor__id=usuario_asociado) |
            Q(gestor__id=usuario_asociado) |
            Q(abogado__id=usuario_asociado)
        )

    # Paginación
    page = request.GET.get('page', 1)
    paginator = Paginator(contratos, 20)  # 10 contratos por página
    try:
        contratos_paginados = paginator.page(page)
    except PageNotAnInteger:
        contratos_paginados = paginator.page(1)
    except EmptyPage:
        contratos_paginados = paginator.page(paginator.num_pages)

    contratos_data = []
    for contrato in contratos_paginados:
        if contrato.plazo_fin:
            dias_restantes = (contrato.plazo_fin - hoy).days
            estado = 'activo' if dias_restantes > 0 else 'finalizado'
        else:
            dias_restantes = None
            estado = 'sin fecha de finalización'

        contratos_data.append({
            'numero_contrato': contrato.numero_contrato,
            'objeto': contrato.objeto,
            'plazo_fin': contrato.plazo_fin.isoformat() if contrato.plazo_fin else None,
            'dias_restantes': dias_restantes,
            'estado': estado,
        })
    
    contratos_json = json.dumps(contratos_data, default=str)
    
    # Obtener opciones para los filtros
    supervisores = Supervisor.objects.all()
    contratistas = Contratista.objects.all()
    usuarios = User.objects.all()

    context = {
        'hoy': hoy,
        'contratos': contratos_paginados,
        'contratos_json': contratos_json,
        'supervisores': supervisores,
        'contratistas': contratistas,
        'usuarios': usuarios,
    }
    
    return render(request, 'contract/contract.html', context)

@login_required
def contratodetailsview(request, contrato_id):
    contrato = get_object_or_404(Contrato, id=contrato_id)
    supervisores = Supervisor.objects.all()
    contratistas = Contratista.objects.all()
    usuarios = User.objects.all()

    if request.method == 'POST':
        form = ContratoForm(request.POST, instance=contrato)
        if form.is_valid():
            contrato_actualizado = form.save(commit=False)
            
            # Actualizar campos relacionados
            contrato_actualizado.supervisor_id = request.POST.get('supervisor')
            contrato_actualizado.contratista_id = request.POST.get('contratista')
            contrato_actualizado.gestor_id = request.POST.get('gestor')
            contrato_actualizado.abogado_id = request.POST.get('abogado')
            contrato_actualizado.revisor_id = request.POST.get('revisor')
            
            # Manejar el campo 'almacen' que es un booleano
            contrato_actualizado.almacen = 'almacen' in request.POST
            
            contrato_actualizado.save()
            messages.success(request, 'El contrato ha sido actualizado con éxito.')
            return redirect('contrato_detalle', contrato_id=contrato.id)
        else:
            messages.error(request, 'Hubo un error al actualizar el contrato. Verifica los campos.')
            print(form.errors)  # Imprimir errores para depuración
    else:
        form = ContratoForm(instance=contrato)

    context = {
        'contrato': contrato,
        'form': form,
        'supervisores': supervisores,
        'contratistas': contratistas,
        'usuarios': usuarios,
    }
    return render(request, 'contract/contract_detail.html', context)

@login_required
def borrar_contrato(request, contrato_id):
    contrato = get_object_or_404(Contrato, id=contrato_id)
    if request.method == 'POST':
        contrato.delete()
        messages.success(request, 'El contrato ha sido eliminado con éxito.')
        return redirect('contrato')
    else:
        messages.error(request, 'No se puede eliminar el contrato.')
    
    return redirect('contrato_detalle', contrato_id=contrato.id)

# Personal ---------------------------------------------------------------------------------------------------------------------
@login_required
def personalview(request):
    supervisores = Supervisor.objects.all()
    contratistas = Contratista.objects.all()
    context={
        'supervisores': supervisores,
        'contratistas': contratistas,
    }
    return render(request, 'personal/gestion_personal.html', context )

@login_required
def personal_s_view(request):
    if request.method == 'POST':
        form = SupervisorForm(request.POST)
        if form.is_valid():
            form.save()
            print('SI FUNCIONO')
            print(form)
            messages.success(request, 'El Supervisor ha sido creado con éxito.')
            return redirect('sp')  # Redirige a la misma página o a donde desees
        else:
            messages.error(request, 'Hubo un error al crear el Supervisor. Verifica los campos.')
    else:
        form = SupervisorForm()
    context={
        'form': form
    }
    return render(request, 'personal/create_supervisor.html', context)

@login_required
def personal_p_view(request):
    if request.method == 'POST':
        form = ContratistaForm(request.POST)
        if form.is_valid():
            form.save()
            print('SI FUNCIONO')
            print(form)
            messages.success(request, 'El Contratista ha sido creado con éxito.')
            return redirect('sp')  # Redirige a la misma página o a donde desees
        else:
            messages.error(request, 'Hubo un error al crear el Contratista. Verifica los campos.')
    else:
        form = ContratistaForm()
    context={
        'form': form
    }
    return render(request, 'personal/create_contratista.html', context)

@login_required
def personal_s_update(request, supervisor_id):
    supervisor = get_object_or_404(Supervisor, id=supervisor_id)
    if request.method == 'POST':
        form = SupervisorForm(request.POST, instance=supervisor)
        if form.is_valid():
            form.save()
            messages.success(request, 'El Supervisor ha sido actualizado con éxito.')
            return redirect('sp')
        else:
            messages.error(request, 'Hubo un error al actualizar el Supervisor. Verifica los campos.')
    else:
        form = SupervisorForm(instance=supervisor)
    context = {
        'form': form,
        'supervisor': supervisor
    }
    return render(request, 'personal/update_supervisor.html', context)

@login_required
def personal_p_update(request, contratista_id):
    contratista = get_object_or_404(Contratista, id=contratista_id)
    if request.method == 'POST':
        form = ContratistaForm(request.POST, instance=contratista)
        if form.is_valid():
            form.save()
            messages.success(request, 'El Contratista ha sido actualizado con éxito.')
            return redirect('sp')
        else:
            messages.error(request, 'Hubo un error al actualizar el Contratista. Verifica los campos.')
    else:
        form = ContratistaForm(instance=contratista)
    context = {
        'form': form,
        'contratista': contratista
    }
    return render(request, 'personal/update_contratista.html', context)

@login_required
def personal_s_delete(request, supervisor_id):
    supervisor = get_object_or_404(Supervisor, id=supervisor_id)
    if request.method == 'POST':
        supervisor.delete()
        print(f"El supervisor con ID {supervisor_id} ha sido eliminado.")
        messages.success(request, 'El Supervisor ha sido eliminado con éxito.')
        return redirect('sp')  # Redirige a la lista de supervisores
    else:
        print(f"El supervisor con ID {supervisor_id} no ha sido eliminado.")
        messages.error(request, 'No se puede eliminar el Supervisor.')
    return render(request, 'personal/update_supervisor.html')

@login_required
def personal_p_delete(request, contratista_id):
    contratista = get_object_or_404(Contratista, id=contratista_id)
    if request.method == 'POST':
        contratista.delete()
        print(f"El supervisor con ID {contratista_id} ha sido eliminado.")
        messages.success(request, 'El Contratista ha sido eliminado con éxito.')
        return redirect('sp')  # Redirige a la lista de contratistas
    else:
        print(f"El supervisor con ID {contratista_id} NO sido eliminado.")
        messages.error(request, 'No se puede eliminar el Contratista.')
    return redirect('sp')

# ---------------------------- FUNCIONAMIENTO ----------------------------
# Estas vistas realizan procesos que no terminan en un render, sino que
# ejecutan tareas de "backend". Su propósito es llevar a cabo operaciones
# en el servidor sin generar una respuesta visual directa para el usuario.
# -----------------------------------------------------------------------
@login_required
def exportar_contratos_csv(request):
    # Definir la respuesta como un archivo CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="contratos.csv"'

    # Crear el escritor de CSV
    writer = csv.writer(response)
    
    # Escribir la fila de encabezados
    writer.writerow([
        'Número de Contrato', 'Tipo de Contratación', 'Descripción', 'Clase de Contrato', 'Valor Final del Contrato',
        'Fecha Suscripción Contrato', 'CDP Número', 'CDP Fecha', 'RP Número', 'RP Fecha', 'Rubro Presupuestal',
        'Número Póliza', 'Fuente Recursos SIGEP', 'Plazo Inicio', 'Plazo Fin', 'Estado del Contrato',
        'Fecha Publicación SECOP', 'Publicación SECOP', 'Almacén', 'Fecha Liquidación'
    ])

    # Obtener los contratos de la base de datos
    contratos = Contrato.objects.all()

    # Escribir los datos de cada contrato en una fila
    for contrato in contratos:
        writer.writerow([
            contrato.numero_contrato, contrato.tipo_contratacion, contrato.descripcion,
            contrato.clase, contrato.valor, contrato.fecha_suscripcion_contrato.strftime("%d/%m/%Y") if contrato.fecha_suscripcion_contrato else '',
            contrato.CDP_num, contrato.CDP_fecha.strftime("%d/%m/%Y") if contrato.CDP_fecha else '',
            contrato.RP_num, contrato.RP_fecha.strftime("%d/%m/%Y") if contrato.RP_fecha else '',
            contrato.rubro_presupuestal, contrato.numero_poliza, contrato.fuente_recursos,
            contrato.plazo_inicio.strftime("%d/%m/%Y") if contrato.plazo_inicio else '',
            contrato.plazo_fin.strftime("%d/%m/%Y") if contrato.plazo_fin else '',
            contrato.estado_contrato, 
            contrato.fecha_publicacion_secop.strftime("%d/%m/%Y") if contrato.fecha_publicacion_secop else '',
            contrato.publicacion_secop, 'Sí' if contrato.almacen else 'No',
            contrato.fecha_liquidacion.strftime("%d/%m/%Y") if contrato.fecha_liquidacion else ''
        ])

    return response

