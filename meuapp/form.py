from django import forms


class Formulario(forms.Form):
    documento = forms.FileField(label="Selecione o arquivo CNAB")
