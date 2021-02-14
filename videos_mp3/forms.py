from django import forms


class Form_Descarga(forms.Form):
    url = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Ingresa la URL del Vídeo'}), label=False)