from django.urls import path
from . import views

urlpatterns = [
    path('contratos/', views.contratosview, name='contrato'),
    path('crear-contrato/', views.crear_contrato, name='crear_contrato'),
    path('personal/', views.personalview, name='sp'),
    path('crear-supervisor/', views.personal_s_view, name='create-s'),
    path('crear-contratista/', views.personal_p_view, name='create-p'),
    path('exportar-contratos/', views.exportar_contratos_csv, name='exportar_contratos'),
    path('contrato/<int:contrato_id>/', views.contratodetailsview, name='contrato_detalle'),
]