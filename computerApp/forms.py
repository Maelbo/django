from jsonschema import ValidationError
from computerApp.models import Machine
from django import forms

class AddMachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ('nom', 'responsable', 'maintenanceDate')
    
