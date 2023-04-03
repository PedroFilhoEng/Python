from django.forms import ModelForm
from app.models import Cliente
import datetime
# Create the form class.
class ClienteForm(ModelForm):
        class Meta:
            model = Cliente
            fields = ['Nome', 'Brinde', 'Sala']




