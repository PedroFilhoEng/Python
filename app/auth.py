from django.contrib.auth.models import Permission

# Renomeie 'delete_cliente' para 'delete_cliente_custom'
perm = Permission.objects.create(codename='delete_cliente_custom', name='Can delete cliente')
