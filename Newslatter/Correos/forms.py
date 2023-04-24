from django import forms
from Suscripcion.models import Email

class FormularioContacto(forms.Form):
    todos = forms.BooleanField(required=False)
    correos = forms.ModelMultipleChoiceField(
    queryset=Email.objects.values_list('email', flat=True),
    widget=forms.CheckboxSelectMultiple(attrs={'value': '%(value)s'}),
    to_field_name='email',
    required=False
)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['correos'].queryset = Email.objects.all()
    
  
    contenido=forms.CharField(label="contenido", widget=forms.Textarea)
    archivo_adjunto = forms.FileField(required=False)
    fecha_hora = forms.DateTimeField(label='Fecha y hora de envío programado', 
                                      widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))





   