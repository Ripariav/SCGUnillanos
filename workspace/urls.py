from django.urls import path
from . import views

urlpatterns = [
    # Contratos ======================================================================================================================================
    path('contratos/', views.contratosview, name='contrato'),
    path('crear-contrato/', views.crear_contrato, name='crear_contrato'),
    path('exportar-contratos/', views.exportar_contratos_csv, name='exportar_contratos'),
    path('contrato/<int:contrato_id>/', views.contratodetailsview, name='contrato_detalle'),
    path('borrar-contrato/<int:contrato_id>/', views.borrar_contrato, name='borrar_contrato'),
    
    # Modificaciones de Contrato ---
    path('contrato/<int:contrato_id>/adicion/', views.crear_adicion, name='crear_adicion'),
    path('contrato/<int:contrato_id>/prorroga/', views.crear_prorroga, name='crear_prorroga'),
    path('contrato/<int:contrato_id>/modificacion/', views.crear_modificacion, name='crear_modificacion'),
    path('contrato/<int:contrato_id>/aclaracion/', views.crear_aclaracion, name='crear_aclaracion'),
    path('contrato/<int:contrato_id>/adicion/borrar/<int:adicion_id>/', views.borrar_adicion, name='borrar_adicion'),
    path('contrato/<int:contrato_id>/prorroga/borrar/<int:prorroga_id>/', views.borrar_prorroga, name='borrar_prorroga'),
    path('contrato/<int:contrato_id>/modificacion/borrar/<int:modificacion_id>/', views.borrar_modificacion, name='borrar_modificacion'),
    path('contrato/<int:contrato_id>/aclaracion/borrar/<int:aclaracion_id>/', views.borrar_aclaracion, name='borrar_aclaracion'),
    path('contrato/<int:contrato_id>/editar/', views.contrato_update_view, name='contrato_editar'),

    # Alteraciones de Contrato
    path('contrato/<int:contrato_id>/suspension/', views.crear_suspension, name='crear_suspension'),
    path('contrato/<int:contrato_id>/reinicio/', views.crear_reinicio, name='crear_reinicio'),
    path('contrato/<int:contrato_id>/ampliacion/', views.crear_ampliacion, name='crear_ampliacion'),
    path('contrato/<int:contrato_id>/suspension/borrar/<int:suspension_id>/', views.borrar_suspension, name='borrar_suspension'),
    path('contrato/<int:contrato_id>/reinicio/borrar/<int:reinicio_id>/', views.borrar_reinicio, name='borrar_reinicio'),
    path('contrato/<int:contrato_id>/ampliacion/borrar/<int:ampliacion_id>/', views.borrar_ampliacion, name='borrar_ampliacion'),

    # Personal ======================================================================================================================================
    path('personal/', views.personalview, name='sp'),
    path('tipocontratista/', views.tipocontratista, name='tipocontratista'),
    path('crear-supervisor/', views.personal_s_view, name='create-s'),
    path('editar-supervisor/<int:supervisor_id>/', views.personal_s_update, name='editar_supervisor'),
    path('borrar-supervisor/<int:supervisor_id>/', views.personal_s_delete, name='borrar_supervisor'),
    path('crear-contratista/', views.personal_c_view, name='create-c'),
    path('crear-contratista-pn/', views.personal_c_pn_view, name='create-c-pn'),
    path('editar-contratista/<int:contratista_id>/', views.personal_c_update, name='editar_contratista'),
    path('borrar-contratista/<int:contratista_id>/', views.personal_c_delete, name='borrar_contratista'),
]