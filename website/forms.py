from django import forms
from .models import Cliente


""" class CrearClienteForm(forms.ModelForm):
    nombre = forms.ChoiceField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Nombres", "class":"form-control"}), label=" ")
    apellido = forms.ChoiceField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Apellidos", "class":"form-control"}), label="")
    pais = forms.ChoiceField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Pais", "class":"form-control"}), label="")
    ciudad = forms.ChoiceField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Ciudad", "class":"form-control"}), label="")
    numero = forms.ChoiceField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Numero", "class":"form-control"}), label="")
    correo = forms.ChoiceField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Correo", "class":"form-control"}), label="")
    
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'pais', 'ciudad', 'numero', 'correo'] 
        #exclude = ("user",)

from django import forms
from .models import Cliente """

class CrearClienteForm(forms.ModelForm):
    nombre = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Nombres", "class": "form-control"}),
        label=" "
    )
    apellido = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Apellidos", "class": "form-control"}),
        label=""
    )
    pais = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Pais", "class": "form-control"}),
        label=""
    )
    ciudad = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Ciudad", "class": "form-control"}),
        label=""
    )
    numero = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Numero", "class": "form-control"}),
        label=""
    )
    correo = forms.EmailField(
        required=True,
        widget=forms.widgets.EmailInput(attrs={"placeholder": "Correo", "class": "form-control"}),
        label=""
    )
    
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'pais', 'ciudad', 'numero', 'correo']
