from django.db import models
import uuid
import datetime



# Managers
from .managers import (
    ClienteManager,
    ExistenciaManager,
    ProductoManager,
    FolioManager
    )

class DescuentoPorVolumen(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    descuento = models.DecimalField(max_digits=19, decimal_places=2)
    activo = models.BooleanField(default=True)
    importe = models.DecimalField(max_digits=19, decimal_places=2)

    date_created = models.DateTimeField(auto_now_add=True)
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'descuento_por_volumen'

class Marca(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    activa = models.BooleanField(default=True)
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()
    marca = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'marca'

class Linea(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    activa = models.BooleanField(default=True)
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()
    linea = models.CharField(unique=True, max_length=50)
    descripcion = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'linea'

class Clase(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    activa = models.BooleanField(default=True)
    clase = models.CharField(unique=True, max_length=50)
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'clase'

class Producto(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    acabado = models.CharField(max_length=20, blank=True, null=True)
    activo = models.BooleanField(default=True)
    ajuste = models.BigIntegerField()
    ancho = models.DecimalField(db_column='ANCHO', max_digits=19, decimal_places=3) 
    calibre = models.DecimalField(max_digits=19, decimal_places=2)
    caras = models.IntegerField()
    clase = models.ForeignKey(Clase, models.DO_NOTHING, blank=True, null=True)
    clave = models.CharField(max_length=255)
    codigo = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=15, blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField()
    de_linea = models.BooleanField(default=True)
    descripcion = models.CharField(max_length=255)
    fecha_lista = models.DateTimeField(blank=True, null=True)
    gramos = models.DecimalField(max_digits=19, decimal_places=2)
    inventariable =models.BooleanField(default=True)
    kilos = models.DecimalField(max_digits=19, decimal_places=3)
    largo = models.DecimalField(max_digits=19, decimal_places=3)
    last_updated = models.DateTimeField()
    linea = models.ForeignKey(Linea, models.DO_NOTHING, blank=True, null=True)
    m2xmillar = models.DecimalField(max_digits=19, decimal_places=3)
    marca = models.ForeignKey(Marca, models.DO_NOTHING, blank=True, null=True)
    modo_venta = models.CharField(max_length=1)
    nacional = models.BooleanField(default=True)
    precio_contado = models.DecimalField(max_digits=19, decimal_places=2)
    precio_credito = models.DecimalField(max_digits=19, decimal_places=2)
    presentacion = models.CharField(max_length=9)
    proveedor_favorito = models.ForeignKey('Proveedor', models.DO_NOTHING, blank=True, null=True)
    sw2 = models.BigIntegerField(blank=True, null=True)
    unidad = models.CharField(max_length=10)
    clase = models.CharField(db_column='clase', max_length=255, blank=True, null=True)  
    linea = models.CharField(db_column='linea', max_length=255, blank=True, null=True)  
    marca = models.CharField(db_column='marca', max_length=255, blank=True, null=True)  
    producto_sat = models.ForeignKey('ProductoSat', models.DO_NOTHING, blank=True, null=True)
    unidad_sat = models.ForeignKey('UnidadSat', models.DO_NOTHING, blank=True, null=True)
    grupo_id = models.CharField(max_length=255, blank=True, null=True)

    objects = ProductoManager()

    class Meta:
        managed = False
        db_table = 'producto'

class Proveedor(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    activo = models.BooleanField(default=True)
    clave = models.CharField(unique=True, max_length=255)
    cuenta_bancaria = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()
    nacional = models.BooleanField(default=True)
    nombre = models.CharField(unique=True, max_length=255)
    rfc = models.CharField(max_length=13)
    sw2 = models.BigIntegerField(blank=True, null=True)
    telefono1 = models.CharField(max_length=30, blank=True, null=True)
    telefono2 = models.CharField(max_length=30, blank=True, null=True)
    telefono3 = models.CharField(max_length=30, blank=True, null=True)
    tipo = models.CharField(max_length=26)
    direccion_calle = models.CharField(max_length=200, blank=True, null=True)
    direccion_codigo_postal = models.CharField(max_length=255, blank=True, null=True)
    direccion_colonia = models.CharField(max_length=255, blank=True, null=True)
    direccion_estado = models.CharField(max_length=255, blank=True, null=True)
    direccion_latitud = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    direccion_longitud = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    direccion_municipio = models.CharField(max_length=255, blank=True, null=True)
    direccion_numero_exterior = models.CharField(max_length=50, blank=True, null=True)
    direccion_numero_interior = models.CharField(max_length=50, blank=True, null=True)
    direccion_pais = models.CharField(max_length=100, blank=True, null=True)
    plazo = models.IntegerField()
    fecha_revision = models.IntegerField(blank=True, null=True)
    imprimir_costo = models.IntegerField(blank=True, null=True)
    descuentof = models.BigIntegerField(blank=True, null=True)
    diasdf = models.BigIntegerField(blank=True, null=True)
    limite_de_credito = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedor'
    
class ProductoSat(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    clave_prod_serv = models.CharField(unique=True, max_length=255)
    descripcion = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'producto_sat'

class UnidadSat(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    clave_unidad_sat = models.CharField(max_length=255, blank=True, null=True)
    unidad_sat = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unidad_sat'

class Cliente(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    activo = models.BooleanField(default=True)
    cheque_devuelto = models.DecimalField(max_digits=19, decimal_places=2)
    clave = models.CharField(max_length=255)
    date_created = models.DateTimeField(blank=True, null=True)
    foliorfc = models.BigIntegerField()
    forma_de_pago = models.BigIntegerField()
    juridico = models.BooleanField(default=False)
    last_updated = models.DateTimeField(blank=True, null=True)
    nombre = models.CharField(max_length=255)
    permite_cheque = models.BooleanField(default=False)
    rfc = models.CharField(max_length=13)
    sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING, blank=True, null=True)
    sw2 = models.BigIntegerField(blank=True, null=True)
    vendedor = models.ForeignKey('Vendedor', models.DO_NOTHING, blank=True, null=True)
    direccion_calle = models.CharField(max_length=200, blank=True, null=True)
    direccion_codigo_postal = models.CharField(max_length=255, blank=True, null=True)
    direccion_colonia = models.CharField(max_length=255, blank=True, null=True)
    direccion_estado = models.CharField(max_length=255, blank=True, null=True)
    direccion_latitud = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    direccion_longitud = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    direccion_municipio = models.CharField(max_length=255, blank=True, null=True)
    direccion_numero_exterior = models.CharField(max_length=50, blank=True, null=True)
    direccion_numero_interior = models.CharField(max_length=50, blank=True, null=True)
    direccion_pais = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)

    objects = ClienteManager()

    class Meta:
        managed = False
        db_table = 'cliente'



class Sucursal(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    activa = models.BooleanField(default=True)
    clave = models.CharField(unique=True, max_length=20)
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()
    nombre = models.CharField(unique=True, max_length=255)
    sw2 = models.BigIntegerField(blank=True, null=True)
    direccion_calle = models.CharField(max_length=200, blank=True, null=True)
    direccion_codigo_postal = models.CharField(max_length=255, blank=True, null=True)
    direccion_colonia = models.CharField(max_length=255, blank=True, null=True)
    direccion_estado = models.CharField(max_length=255, blank=True, null=True)
    direccion_latitud = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    direccion_longitud = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    direccion_municipio = models.CharField(max_length=255, blank=True, null=True)
    direccion_numero_exterior = models.CharField(max_length=50, blank=True, null=True)
    direccion_numero_interior = models.CharField(max_length=50, blank=True, null=True)
    direccion_pais = models.CharField(max_length=100, blank=True, null=True)
    almacen = models.BooleanField(default=False)
    db_url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'sucursal'

class Vendedor(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    activo =  models.BooleanField(default=True)
    apellido_materno = models.CharField(max_length=255, blank=True, null=True)
    apellido_paterno = models.CharField(max_length=255, blank=True, null=True)
    comision_contado = models.DecimalField(max_digits=19, decimal_places=2)
    comision_credito = models.DecimalField(max_digits=19, decimal_places=2)
    curp = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()
    nombres = models.CharField(max_length=255, blank=True, null=True)
    rfc = models.CharField(max_length=255, blank=True, null=True)
    sw2 = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendedor'

class ClienteCredito(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    atraso_maximo = models.BigIntegerField()
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING)
    cobrador = models.ForeignKey('Cobrador', models.DO_NOTHING, blank=True, null=True)
    credito_activo = models.BooleanField(default=False)
    descuento_fijo = models.DecimalField(max_digits=19, decimal_places=2)
    dia_cobro = models.BigIntegerField()
    dia_revision = models.BigIntegerField()
    linea_de_credito = models.DecimalField(max_digits=19, decimal_places=2)
    operador = models.BigIntegerField()
    plazo = models.BigIntegerField()
    postfechado = models.BooleanField(default=False)
    revision = models.BooleanField(default=False)
    saldo = models.DecimalField(max_digits=19, decimal_places=2)
    socio = models.ForeignKey('Socio', models.DO_NOTHING, blank=True, null=True)
    sw2 = models.BigIntegerField(blank=True, null=True)
    vence_factura = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'cliente_credito'


class Cobrador(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    activo = models.BooleanField(default=True)
    apellido_materno = models.CharField(max_length=255, blank=True, null=True)
    apellido_paterno = models.CharField(max_length=255, blank=True, null=True)
    clave = models.CharField(max_length=255, blank=True, null=True)
    comision = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    curp = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    nombres = models.CharField(max_length=255, blank=True, null=True)
    rfc = models.CharField(max_length=255, blank=True, null=True)
    sw2 = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cobrador'

class Socio(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    clave = models.CharField(max_length=255)
    sw2 = models.BigIntegerField(blank=True, null=True)
    vendedor = models.ForeignKey('Vendedor', models.DO_NOTHING, blank=True, null=True)
    nombre = models.CharField(max_length=255)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING)
    comision_cobrador = models.DecimalField(max_digits=19, decimal_places=2)
    comision_vendedor = models.DecimalField(max_digits=19, decimal_places=2)
    direccion = models.CharField(max_length=255)
    direccion_fiscal_numero_exterior = models.CharField(max_length=50, blank=True, null=True)
    direccion_fiscal_numero_interior = models.CharField(max_length=50, blank=True, null=True)
    direccion_fiscal_latitud = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    direccion_fiscal_longitud = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    direccion_fiscal_estado = models.CharField(max_length=255, blank=True, null=True)
    direccion_fiscal_pais = models.CharField(max_length=100, blank=True, null=True)
    direccion_fiscal_calle = models.CharField(max_length=200, blank=True, null=True)
    direccion_fiscal_colonia = models.CharField(max_length=255, blank=True, null=True)
    direccion_fiscal_codigo_postal = models.CharField(max_length=255, blank=True, null=True)
    direccion_fiscal_municipio = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'socio'

class Existencia(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    entrada_compra = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=19, decimal_places=2)
    movimiento_almacen = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    kilos = models.DecimalField(max_digits=19, decimal_places=2)
    devolucion_venta = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    venta = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING)
    transformacion = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    nacional = models.BooleanField(default=True)
    pedidos_pendiente = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    mes = models.BigIntegerField()
    devolucion_compra = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    producto = models.ForeignKey(Producto, models.DO_NOTHING)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    traslado = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    anio = models.BigIntegerField()
    existencia_inicial = models.DecimalField(max_digits=19, decimal_places=3, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    clave = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    sucursal_nombre = models.CharField(max_length=255, blank=True, null=True)
    recorte = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    recorte_comentario = models.CharField(max_length=255, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    recorte_fecha = models.DateField(blank=True, null=True)
    costo_promedio = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    costo = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

    objects = ExistenciaManager()

    class Meta:
        managed = False
        db_table = 'existencia'


class Folio(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    entidad = models.CharField(max_length=255, blank=True, null=True)
    folio = models.BigIntegerField()
    serie = models.CharField(max_length=255, blank=True, null=True)
    objects = FolioManager()
    class Meta:
        managed = False
        db_table = 'folio'

