from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(label='Nombre', required=True, max_length=100)
    email = forms.CharField(label='Email', required=True, max_length=100)
    consulta = forms.CharField(label='Consulta', widget=forms.Textarea, max_length=600)
