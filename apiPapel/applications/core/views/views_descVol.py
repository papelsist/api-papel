from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView
)
from ..models import DescuentoPorVolumen
from ..serializers import DescuentoPorVolumenSerializer

# Create your views here.

# CRUD Descuento Por Volumen
class ListDescPorVolumen(ListAPIView):
    serializer_class =  DescuentoPorVolumenSerializer
    def get_queryset(self):
        return DescuentoPorVolumen.objects.all()

class DetailDescPorVolumen(RetrieveAPIView):
    serializer_class = DescuentoPorVolumenSerializer
    queryset = DescuentoPorVolumen.objects.all()
    
class CreateDescPorVolumen (CreateAPIView):
    serializer_class = DescuentoPorVolumenSerializer

class DeleteDescPorVolumen (DestroyAPIView):
    serializer_class = DescuentoPorVolumenSerializer
    queryset = DescuentoPorVolumen.objects.all()

class UpdateDescPorVolumen (UpdateAPIView):
    serializer_class = DescuentoPorVolumenSerializer
    queryset = DescuentoPorVolumen.objects.all()

class RetrieveUpdateDescPorVolumen (RetrieveUpdateAPIView):
    # Esta vista permite los verbos GET y PUT 
    serializer_class = DescuentoPorVolumenSerializer
    queryset = DescuentoPorVolumen.objects.all()


