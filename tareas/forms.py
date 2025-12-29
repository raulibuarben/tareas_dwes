#Formularios para la aplicación
#Formulario para el alta de alumnado/profesorado

from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Tarea, TareaGrupal, TareaIndividual, Usuario

class RegistroUsuarioForm(forms.ModelForm):
    password1 = forms.CharField(label=_("Contraseña"), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Repetir contraseña"), widget=forms.PasswordInput)
    rol = forms.ChoiceField(label=_("Tipo de usuario"), choices=Usuario.ROLES, widget=forms.RadioSelect)

    class Meta:
        model = Usuario
        fields = ('username', 'first_name', 'last_name', 'email')

    #Comprueba que las contraseñas coinciden
    def clean_password2(self):
        p1 = self.cleaned_data.get('password1')
        p2 = self.cleaned_data.get('password2')
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError(_("Las contraseñas no coinciden."))
        return p2

    #Guarda el usuario con la contraseña hasheada y el rol seleccionado
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.rol = self.cleaned_data['rol']
        if commit:
            user.save()
        return user


# Formulario para la creación de una tarea individual (puede necesitar o no validación de un profesor)
class TareaIndividualForm(forms.ModelForm):
    #Solicitamos el creador de la tarea
    creador = forms.ModelChoiceField(
        queryset=Usuario.objects.all(), 
        required=True,
        label="Creador"
    )

    class Meta:
        model = TareaIndividual
        fields = ['titulo', 'descripcion', 'fecha_recordatorio', 'requiere_validacion', 'profesor', 'alumno', 'creador']
        widgets = {
            'fecha_recordatorio': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
    # Filtra los usuarios por rol en los campos de profesor y alumno
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profesor'].queryset = Usuario.objects.filter(rol=Usuario.profesor)
        self.fields['alumno'].queryset = Usuario.objects.filter(rol=Usuario.alumno)


#Formulario para la creación de una tarea grupal (puede necesitar o no validación de un profesor)
class TareaGrupalForm(forms.ModelForm):
    #Solicitamos el creador de la tarea
    creador = forms.ModelChoiceField(
        queryset=Usuario.objects.all(),  # tu modelo de usuario
        required=True,
        label="Creador"
    )
    
    class Meta:
        model = TareaGrupal
        fields = ['titulo', 'descripcion', 'fecha_recordatorio', 'requiere_validacion', 'profesor', 'alumnos', 'creador']
        widgets = {
            'fecha_recordatorio': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
    # Filtra los usuarios por rol en los campos de profesor y alumnos
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profesor'].queryset = Usuario.objects.filter(rol=Usuario.profesor)
        self.fields['alumnos'].queryset = Usuario.objects.filter(rol=Usuario.alumno)

    