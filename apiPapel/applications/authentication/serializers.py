from rest_framework import serializers


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Producto
        fields= ('__all__')
        #fields= ('clave',)