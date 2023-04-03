from django.db import models
from django.utils import timezone

# Create your models here.
class Cliente(models.Model):
    Nome = models.CharField(max_length=150)
    Brinde = models.CharField(max_length=150)
    Sala = models.CharField(max_length=150)


