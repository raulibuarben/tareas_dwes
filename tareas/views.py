from django.shortcuts import get_object_or_404, render
from django.views.generic.detail import DetailView
from .models import Tarea, TareaGrupal, TareaIndividual, Usuario
from django.views.generic.edit import CreateView
from .forms import RegistroUsuarioForm, TareaGrupalForm, TareaIndividualForm
from django.urls import reverse_lazy

# Create your views here.
#Detalle tarea.
class detalle_tarea(DetailView):
    model = Tarea
    template_name = 'tareas/detalle_tarea.html'
    context_object_name = 'tarea'


#Vista para el formulario de registro de usuarios

class RegistroUsuarioView(CreateView):
    template_name = 'tareas/registro_usuario.html'
    form_class = RegistroUsuarioForm

    def get_success_url(self):
        return self.request.path
    

#Vista para crear una tarea individual
class CrearTareaIndividualView(CreateView):
    model = TareaIndividual
    form_class = TareaIndividualForm
    template_name = 'tareas/crear_tarea_individual.html'
    
    #asignar al creador el usuario que la realiza
    def form_valid(self, form):
        form.instance.creador = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return self.request.path

#Vista para crear una tarea grupal
class CrearTareaGrupalView(CreateView):
    model = TareaGrupal
    form_class = TareaGrupalForm
    template_name = 'tareas/crear_tarea_grupal.html'

    def get_success_url(self):
        return self.request.path


#Vista en la que un usuario puede ver sus datos
def perfil_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    return render(request, 'tareas/perfil_usuario.html', {'usuario': usuario})


#Vista de alumnos y profesores
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'tareas/lista_usuarios.html', {'usuarios': usuarios})   

