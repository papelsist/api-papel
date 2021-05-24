from rest_framework import serializers, pagination

from applications.core.models import (
    Producto, 
    ProductoSat,
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

class ProductoSatSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ProductoSat
        fields= ('__all__')


# Serializer con foreign Key
# Serializer con MethodField
class ProductSerializer(serializers.ModelSerializer):

    producto_sat = ProductoSatSerializer()

    clave_descripcion = serializers.SerializerMethodField();

    class Meta: 
        model = Producto
        fields= (
            'id','clave','descripcion','precio_contado', 'precio_credito','producto_sat', 'clave_descripcion'
        )
    
    def get_clave_descripcion(self, obj):
        return obj.clave + " - " + obj.descripcion
       
class ProductoPagination(pagination.PageNumberPagination):
    page_size= 10
    max_page_size = 100



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
       
       
        

