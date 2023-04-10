from django.forms import ModelForm
from app.models import Cliente
from django import forms

class ClienteForm(ModelForm):
        class Meta:
            model = Cliente
            fields = ['Nome', 'Brinde', 'Sala']


GEEKS_CHOICES =(
    ("1", "GM - PEDRAS ALTAS"),
    ("2", "GM - STILO BORGES"),
    ("3", "GM - GOLDEN GRAMADO"),
    ("4", "CN - LAGHETTO VIVERONE"),
    ("5", "CN - CATEDRAL"),
    ("6", "BT - LAGHETTO VIVERONE"),
)
class GEEKS_CHOICES(forms.Form):
    geeks_field = forms.ChoiceField(choices = GEEKS_CHOICES)





