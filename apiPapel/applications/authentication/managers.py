from django.db import models


"""  Manager para el modelo Usuario"""
class UsuarioManager(models.Manager):
    def listarUsuarios(self):
        return self.all()

