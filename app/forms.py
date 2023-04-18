from django.forms import ModelForm
from app.models import Cliente
from django.contrib.auth.models import Group, Permission


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['Nome', 'Brinde', 'Sala']


# GEEKS_CHOICES = (
#    ("1", "BT - LAGHETTO VIVERONE"),
#    ("2", "CN - CATEDRAL"),
#    ("3", "CN - LAGHETTO VIVERONE"),
#    ("4", "GM - GOLDEN GRAMADO"),
#    ("5", "GM - PEDRAS ALTAS"),
#    ("6", "GM - STILO BORGES"),
# )


# class GeeksChoicesForm(forms.Form):
#    geeks_field = forms.ChoiceField(choices=GEEKS_CHOICES)


# Criando um grupo de usuários com acesso à área administrativa
admin_group, created = Group.objects.get_or_create(name='Admins')

# Adicionando permissões ao grupo de usuários
permissions = ['add_user', 'change_user', 'delete_user']
for permission in permissions:
    admin_group.permissions.add(Permission.objects.get(codename=permission))

# Configurando o sistema de autenticação do Django
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'path.to.your.custom.AuthBackend',
]