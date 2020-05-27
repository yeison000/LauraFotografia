from django import forms
from fotoapp.models import Contacto


class ContactoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class']= 'form-control' 
            form.field.widget.attrs['autocomplete']= 'off'
        

    class Meta:
        model = Contacto

        fields = '__all__'

        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'placeholder':'Ingrese el nombre',
                    'id': 'nombre'
                }
            ),
        

        'email': forms.EmailInput(
                attrs = {
                    'placeholder':'Ingrese el email',
                    'id': 'email'
                }
            ),
        

        'telefono': forms.NumberInput(
                attrs = {
                    'placeholder':'Ingrese el telefono',
                    'id': 'telefono'
                }
            ),

        'respuesta1': forms.Textarea(
                attrs = {
                    'placeholder':'¿cuando es vuestro gran dia y a que hora?',
                    'rows':1,
                    'cols':1,
                    'id': 'respuesta1'
                }
            ),

        'respuesta2': forms.Textarea(
                attrs = {
                    'placeholder':'¿Donde será la ceremonia y donde la celebraran?(si son varios sitios, dimelo en orden)',
                    'rows':2,
                    'cols':2,
                    'id': 'respuesta2'
                }
            ),

        'respuesta3': forms.Textarea(
                attrs = {
                    'placeholder':'¿Cuantos invitados seréis?(aproximadamente)',
                    'rows':1,
                    'cols':1,
                    'id': 'respuesta3'
                }
            ),

        'respuesta4': forms.Textarea(
                attrs = {
                    'placeholder':'¿que pack sería el que más se adapta a vuestra necesidad?',
                    'rows':2,
                    'cols':2,
                    'id': 'respuesta4'
                }
            ),

        'respuesta5': forms.Textarea(
                attrs = {
                    'placeholder':'¿Alguna duda o pregunta?, estare encantada de responderte!...(opcional)',
                    'rows':3,
                    'cols':3,
                    'id': 'respuesta5'
                }
            ),
        }

    



        