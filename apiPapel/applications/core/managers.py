from django.db import models
from django.db.models import Sum

"""  Manager para el modelo Producto"""
class ProductoManager(models.Manager):

    def listarProductos(self):
        return self.all()

    def buscarProducto(self, prod):     
        resultado = self.filter(
           models.Q(clave__icontains=prod) | models.Q(descripcion__icontains=prod) 
        )
        return resultado

""" Manager para el modelo de Cliente"""
class ClienteManager(models.Manager):
    
    def listarClientes(self):
        return self.all()

    def buscarCliente(self, client):
        resultado = self.filter(
           models.Q(clave__icontains=client) | models.Q(nombre__icontains=client) | models.Q(rfc__icontains=client) 
        )
        return resultado

""" Manager para la existencia"""
class ExistenciaManager(models.Manager):

    def existenciaPorProducto(self, producto, mes, year):   
        return self.filter(producto__id = producto, mes= mes , anio = year)

    def totalExistenciaPorProducto(self, producto, mes, year):   
        return self.filter(producto__id = producto, mes= mes , anio = year).aggregate(Sum('cantidad'))

""" Manager para la folio"""
class FolioManager(models.Manager):

    def getFolioCurrent(self, serie, entidad):   
        return self.filter( serie= serie , entidad = entidad)

    


