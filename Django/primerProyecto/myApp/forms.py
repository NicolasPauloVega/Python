#Se importa el modulo forms de Django, que nos ayuda a crear formulatios html.
from django import forms
#Importamos de myApp el modelo Article
from .models import Article

#creamos una clase la cual hereda de forms.modelForm el modelo Article
class formularioArticulo(forms.ModelForm):
    # Se crea una sub clase que tiene los datos del formulario
    class Meta:
        #Se especifica el modelo que se va a asociar con el formulario
        model = Article
        #le decimos a django que vamos a utilizar todos los campos del modelo Article al formulatio
        fields = '__all__'
        #Se usa un widget personalizado para indicar qué tipo de entrada se debe usar para cada campo del formulario en la interfaz.
        widgets = {
            # Widget para ingresar texto con estilo predeterminado
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            # Área de texto con estilo y tamaño predeterminado
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            # Selector de archivo para cargar imágenes
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
            # Casilla de verificación para indicar si es público o no
            'public': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            # Widget para el campo "public", un simple campo de selección para que el usuario indique si es público o privado
            'public': forms.ChoiceField(choices=[(True, 'Public'), (False, 'Private')], widget=forms.RadioSelect(attrs={'class': 'form-check-input'})),
            # Selector de fecha solo para lectura
            'update_date': forms.DateInput(attrs={'class': 'form-control', 'readonly': True}),   
        }
