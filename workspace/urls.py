from django.urls import path
from . import views

urlpatterns = [
    # Contratos
    path('contratos/', views.contratosview, name='contrato'),
    path('crear-contrato/', views.crear_contrato, name='crear_contrato'),
    path('exportar-contratos/', views.exportar_contratos_csv, name='exportar_contratos'),
    path('contrato/<int:contrato_id>/', views.contratodetailsview, name='contrato_detalle'),
    path('borrar-contrato/<int:contrato_id>/', views.borrar_contrato, name='borrar_contrato'),
    
    # Personal
    path('personal/', views.personalview, name='sp'),
    path('crear-supervisor/', views.personal_s_view, name='create-s'),
    path('editar-supervisor/<int:supervisor_id>/', views.personal_s_update, name='editar_supervisor'),
    path('borrar-supervisor/<int:supervisor_id>/', views.personal_s_delete, name='borrar_supervisor'),
    path('crear-contratista/', views.personal_p_view, name='create-p'),
    path('editar-contratista/<int:contratista_id>/', views.personal_p_update, name='editar_contratista'),
    path('borrar-contratista/<int:contratista_id>/', views.personal_p_delete, name='borrar_contratista'),
]