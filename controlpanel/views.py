from django.shortcuts import render, redirect
from workspace.models import Contrato, Rol
from django.contrib.auth.decorators import login_required
from datetime import date
import json


# Create your views here.
@login_required
def homeview(request):
    user = request.user
    hoy = date.today()
    num_contratos_pendientes = 0
    num_cnt_act = 0
    num_precio_act = 0.0
    canti_contratos = 0
    c_dir = 0
    c_priv = 0
    c_pub = 0
    sc = 0

    # Obtener contratos donde el usuario es el gestor, abogado o revisor
    if user.is_staff:
        contratos = Contrato.objects.all()
    else:
        contratos = Contrato.objects.filter(gestor=user) | Contrato.objects.filter(abogado=user) | Contrato.objects.filter(revisor=user)

    contratos_data = []

    for contrato in contratos:
        num_precio_act += float(contrato.valor) if contrato.valor is not None else 0.0
        if contrato.tipo_contratacion:
            if contrato.tipo_contratacion == 'Directa':
                c_dir += 1
            elif contrato.tipo_contratacion == 'Privada':
                c_priv += 1
            elif contrato.tipo_contratacion == 'Publica':
                c_pub += 1
            else:
                sc += 1
        if contrato.plazo_fin:
            canti_contratos += 1
            dias_restantes = (contrato.plazo_fin - hoy).days
            estado = 'activo' if dias_restantes > 0 else 'finalizado'
            if dias_restantes < 0:
                num_contratos_pendientes += 1
            else:
                num_cnt_act += 1
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

    # Datos para el gráfico de barras
    bar_data = {
        'labels': ['Directa', 'Privada', 'Pública', 'Sin Clasificar'],
        'data': [c_dir, c_priv, c_pub, sc]
    }

    # Datos para el gráfico de líneas (ejemplo de días de la semana)
    days_labels = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom']
    line_data = {
        'labels': days_labels,
        'completed': [contratos.filter(plazo_fin__week_day=i).count() for i in range(2, 9)]  # Ajusta según tu lógica
    }

    # Datos para el gráfico de pastel
    pie_data = [
        {'value': num_contratos_pendientes, 'name': 'Pendientes'},
        {'value': num_cnt_act, 'name': 'Activos'},
        {'value': num_precio_act, 'name': 'Precio Total'}
    ]

    context = {
        'contratos': contratos,
        'contratos_json': contratos_json,
        'hoy': hoy,
        'num_contratos_pen': num_contratos_pendientes,
        'num_contratos_act': num_cnt_act,
        'num_precio_act': num_precio_act,
        'canti_contratos': canti_contratos,
        'c_pub': c_pub,
        'c_dir': c_dir,
        'c_priv': c_priv,
        'sc': sc,
        'bar_data': json.dumps(bar_data),
        'line_data': json.dumps(line_data),
        'pie_data': json.dumps(pie_data),
    }
    return render(request, 'panelcontrol/home.html', context)


@login_required
def profileview(request):
    return render(request, 'profile/profile.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST['full_name'].split()[0]
        user.last_name = " ".join(request.POST['full_name'].split()[1:])
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.save()
        return redirect('profile')
    
    return render(request, 'profile/edit_profile.html')

