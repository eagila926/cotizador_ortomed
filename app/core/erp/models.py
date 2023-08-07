from django.db import models

# Create your models here.

class Usuario(models.Model):
    cod_user = models.TextField(max_lenght=150,unique= True, verbose_name='Codigo')
    nombre = models.TextField(max_lenght=150, verbose_name='Nombre')
    apellido = models.TextField(max_lenght=150, verbose_name='Apellido')
    correo = models.TextField(max_lenght=150, verbose_name='Correo')
    tipo = models.TextField(max_lenght=3, verbose_name='Tipo')
    ciudad = models.TextField(max_lenght=3, verbose_name='Ciudad')
    pais = models.TextField(max_lenght=3, verbose_name='Pais')

    def _str_(selfs):
        return selfs.cod_user
    
    class Meta:
        verbose_names = 'Usuario'
        verbose_names_plural = 'Usuarios'
        de_table = 'usuario'
        ordering: ['cod_user']
    

class Activos(models.Model):
    cod_activo = models.TextField(max_length=15,unique=True,verbose_name='Cod Activo')
    descripcion = models.TextField(max_length=200,verbose_name='Descripcion')
    valor_costo = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor Costo')
    valor_venta = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor Venta')
    unidad_compra = models.TextField(max_length=3,verbose_name='Unidad Compra')
    stock = models.DecimalField(max_digits=15, decimal_places=3, verbose_name='Stock')
    stock_min = models.DecimalField(max_digits=15, decimal_places=3,verbose_name='Stock FIn')
    m1 = models.DecimalField(max_digits=15, decimal_places=4,verbose_name='m1')
    m2 = models.DecimalField(max_digits=15, decimal_places=4,verbose_name='m2')
    m3 = models.DecimalField(max_digits=15, decimal_places=4,verbose_name='m3')
    v1 = models.DecimalField(max_digits=15, decimal_places=4,verbose_name='v1')
    v2 = models.DecimalField(max_digits=15, decimal_places=4,verbose_name='v2')
    v3 = models.DecimalField(max_digits=15, decimal_places=4,verbose_name='v3')
    vf1 = models.DecimalField(max_digits=15, decimal_places=4,verbose_name='vf1')
    vf2 = models.DecimalField(max_digits=15, decimal_places=4,verbose_name='vf2')
    vf3 = models.DecimalField(max_digits=15, decimal_places=4,verbose_name='vf3')
    p1 = models.DecimalField(max_digits=15, decimal_places=4,verbose_name='p1')
    p2 = models.DecimalField(max_digits=15, decimal_places=4,verbose_name='p2')
    p3 = models.DecimalField(max_digits=15, decimal_places=4,verbose_name='p3')
    factor = models.DecimalField(_("Factor"), max_digits=15, decimal_places=3)
    densidad = models.DecimalField(max_digits=15, decimal_places=4,verbose_name='Densidad')
    tipo = models.DecimalField(verbose_name='Tipo', max_length=50)

    def _str_(selfs):
        return selfs.cod_activo
    
    class Meta:
        verbose_names = 'Activo'
        verbose_names_plural = 'Activos'
        de_table = 'activo'
        ordering: ['cod_activo']


class Clientes(models.Model):
    nombre = models.TextField(max_length=100, verbose_name="Nombre")
    cedula = models.TextField(max_length=15, verbose_name="Cedula")
    telefono = models.TextField(max_length=100, verbose_name="Telefono")
    correo = models.TextField(max_length=100, verbose_name="correo")
    direccion = models.TextField(max_length=100, verbose_name="Direccion")
    tipo = models.TextField(max_length=100, verbose_name="Tipo")
    cod_user = models.TextField(max_length=100, verbose_name="cod_user")

    def _str_(selfs):
        return selfs.nombre
        
    class Meta:
        verbose_names = 'Cliente'
        verbose_names_plural = 'Clientes'
        de_table = 'cliente'
        ordering: ['Nombre']

class Doctores(models.Model):
    nombre = models.TextField(max_length=150,verbose_name="Nombre")
    telefono = models.TextField(max_length=150,verbose_name="Telefono")
    cedula = models.TextField(max_length=150,verbose_name="cedula")
    direccion = models.TextField(max_length=150,verbose_name="direccion")
    ciudad = models.TextField(max_length=150,verbose_name="Ciudad")
    cod_user = models.TextField(max_length=10,verbose_name="Codigo User")

    def _str_(selfs):
        return selfs.nombre
        
    class Meta:
        verbose_names = 'Doctor'
        verbose_names_plural = 'Doctores'
        de_table = 'doctor'
        ordering: ['Nombre']            
            
            
