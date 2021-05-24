
from django.db import models
import uuid
import datetime
from ..common.NewBooleanField import NewBooleanField
from .managers import UsuarioManager
# Create your models here.


class Usuario(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    account_expired = NewBooleanField(default=False)  # This field type is a guess.
    account_locked = NewBooleanField(default=False)  # This field type is a guess.
    apellido_materno = models.CharField(max_length=255)
    apellido_paterno = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)
    enabled = NewBooleanField(default=True)  # This field type is a guess.
    nombre = models.CharField(max_length=255)
    nombres = models.CharField(max_length=255)
    numero_de_empleado = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=255)
    password_expired = NewBooleanField(default=False)  # This field type is a guess.
    puesto = models.CharField(max_length=30, blank=True, null=True)
    sucursal = models.CharField(max_length=20, blank=True, null=True)
    username = models.CharField(unique=True, max_length=255)
    nip = models.CharField(max_length=12, blank=True, null=True)

    objects = UsuarioManager

    class Meta:
        managed = False
        db_table = 'user'


class Role(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    authority = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'role'



class UsuarioRole(models.Model):
    user = models.OneToOneField(Usuario, models.DO_NOTHING, primary_key=True)
    role = models.ForeignKey(Role, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_role'
        unique_together = (('user', 'role'),)
