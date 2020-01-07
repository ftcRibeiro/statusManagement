from django import forms

from .models import Status, Maquina

class FormStatus(forms.ModelForm):
    class Meta:
        model = Status
        fields = ('nome','codigo',)

class FormMaquina(forms.ModelForm):
    class Meta:
        model: Maquina
        fields = ('nome')