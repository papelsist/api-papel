from django.contrib import admin
from django.urls import path
from .views import (
    views_descVol, 
    views_producto 
)

urlpatterns = [
    # URLS Descuento por Volumen
    path('api/create-descxvolumen/', views_descVol.CreateDescPorVolumen.as_view() ),
    path('api/list-descxvolumen/', views_descVol.ListDescPorVolumen.as_view() ),
    path('api/detail-descxvolumen/<pk>', views_descVol.DetailDescPorVolumen.as_view() ),
    path('api/delete-descxvolumen/<pk>', views_descVol.DeleteDescPorVolumen.as_view() ),
    path('api/update-descxvolumen/<pk>', views_descVol.UpdateDescPorVolumen.as_view() ),
    path('api/modificar-descxvolumen/<pk>', views_descVol.RetrieveUpdateDescPorVolumen.as_view() ),

    # URLS Producto
    path('api/list-producto/', views_producto.ListProducto.as_view() ),
    path('api/list-pagination-producto/', views_producto.PaginationListProducto.as_view() ),

]

