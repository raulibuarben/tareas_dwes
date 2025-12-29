from django.urls import path

from tareas.views import CrearTareaGrupalView, CrearTareaIndividualView, RegistroUsuarioView, detalle_tarea, lista_tareas_usuario, lista_tareas_validacion, lista_usuarios, perfil_usuario

urlpatterns = [
    path('<uuid:pk>/', detalle_tarea.as_view(), name = 'detalle_tarea'),
    path('registro/', RegistroUsuarioView.as_view(), name='registro_usuario'),
    path('crear_tarea_individual/', CrearTareaIndividualView.as_view(), name='crear_tarea_individual'),
    path('crear_tarea_grupal/', CrearTareaGrupalView.as_view(), name='crear_tarea_grupal'),
    path('perfil/<int:pk>/', perfil_usuario, name='perfil_usuario'),
    path('lista_usuarios/', lista_usuarios, name='lista_usuarios'),
    path('lista_tareas_usuario/<int:pk>/', lista_tareas_usuario, name='lista_tareas_usuario'),
    path('lista_tareas_validacion/<int:pk>/', lista_tareas_validacion, name='lista_tareas_validacion'),
]

