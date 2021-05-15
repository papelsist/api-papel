from rest_framework import serializers

from applications.core.models import (
    Producto, 
    DescuentoPorVolumen,
    Cliente,
    ClienteCredito,
    Existencia,
    Folio
    )


class ProductoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Producto
        fields= ('__all__')
        #fields= ('clave',)

class DescuentoPorVolumenSerializer(serializers.ModelSerializer):
    class Meta: 
        model = DescuentoPorVolumen
        fields= ('__all__')

class ClienteSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Cliente
        fields= ('__all__')

class ClienteCreditoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ClienteCredito
        fields= ('__all__')

class ExistenciaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Existencia
        fields= ('__all__')

class FolioSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Folio
        fields= ('__all__')
       
       
        

