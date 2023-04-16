from django.forms import ModelForm

from app.models import Cliente
# from django import forms


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['Nome', 'Brinde', 'Sala']


#GEEKS_CHOICES = (
#    ("1", "BT - LAGHETTO VIVERONE"),
#    ("2", "CN - CATEDRAL"),
#    ("3", "CN - LAGHETTO VIVERONE"),
#    ("4", "GM - GOLDEN GRAMADO"),
#    ("5", "GM - PEDRAS ALTAS"),
#    ("6", "GM - STILO BORGES"),
#)


#class GeeksChoicesForm(forms.Form):
#    geeks_field = forms.ChoiceField(choices=GEEKS_CHOICES)
