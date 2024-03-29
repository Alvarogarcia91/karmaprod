from django.db import models

#Create your models here.
class Espumado(models.Model):
    #fecha que del excel
    fecha_producido = models.CharField(max_length=200)
    #block/cilindro
    forma = models.CharField(max_length=200)
    #Tipo Espuma de excel Block/Cilindros
    tipo_espuma = models.CharField(max_length=200)
    #No. Corrida
    num_corrida = models.IntegerField(blank=True, default=1, null=True)
    #No. Block
    num_block = models.IntegerField(blank=False)
    #Tipo Unidad
    tipo_unidad = models.CharField(max_length=200,blank=True)
    #No. Lote
    no_lote = models.CharField(max_length=200,blank=False)
    #Tipo Ajuste
    tipo_ajuste = models.CharField(max_length=200, blank=True)
    #Tipo Defecto
    #--agregar choices--
    tipo_defecto = models.CharField(max_length=200,blank=True)
    #OK/NG
    ok_ng = models.CharField(max_length=200,blank=False)

    #---Medidas---CAPTURADAS
    #Largo der.
    largo = models.DecimalField(max_digits=10, decimal_places=2,blank = False, null=True)
    #Ancho
    ancho = models.DecimalField(max_digits=10, decimal_places=2,blank = False, null=True)
    #Alto los cilindros no tienen este valor
    alto = models.DecimalField(max_digits=10, decimal_places=2,blank = True, null=True)
    #Flujo de Aire ≥10
    flujo_de_aire = models.IntegerField()
    #Peso
    peso = models.DecimalField(max_digits=6, decimal_places=2,blank = False, null=True)
    #Volumen
    volumen = models.DecimalField(max_digits=6, decimal_places=2,blank = True, null=True)
    #Densidad
    densidad = models.DecimalField(max_digits=6, decimal_places=2,blank = True, null=True)
    #Metros
    #flags indicadores
    auth_corte = models.BooleanField(default = False)
    dispobible =models.BooleanField(default = True)

    #fecha en db
    #fecha_capturado = models.DateTimeField(auto_now_add=True)

#---Medidas---CURADAS
    #Largo der.
    largo_curado = models.DecimalField(max_digits=10, decimal_places=2,blank = False, null=True)
    #Ancho
    ancho_curado = models.DecimalField(max_digits=10, decimal_places=2,blank = False, null=True)
    #Alto los cilindros no tienen este valor
    alto_curado = models.DecimalField(max_digits=10, decimal_places=2,blank = True, null=True)
    #Peso
    peso_curado = models.DecimalField(max_digits=6, decimal_places=2,blank = False, null=True)
    #Volumen
    volumen_curado = models.DecimalField(max_digits=6, decimal_places=2,blank = True, null=True)
    #Densidad
    densidad_curado = models.DecimalField(max_digits=6, decimal_places=2,blank = True, null=True)
    #Metros


    class Meta:
        abstract = True

    def __str__(self):
        return 'Tipo_espuma: {0} lote: {1} num_block: {2} id: {3}'   .format(self.tipo_espuma, self.no_lote,self.num_block,self.id)

class Block(Espumado):
    pass

class Cilindro(Espumado):
    pass

class Aglutinado(Espumado):
    pass


class Device(models.Model):

    type = models.CharField(max_length=200, blank=False)
    price = models.IntegerField()

    choices = (
        ('AVAILABLE', 'Item ready to be purchased'),
        ('SOLD', 'Item already purchased'),
        ('RESTOCKING', 'Item restocking in few days')
    )

    status = models.CharField(max_length=10,choices=choices, default='SOLD')
    issues = models.CharField(max_length=50, default="No Issues")

    class Meta:
        abstract = True

    def __str__(self):
        return 'Type: {0} Price: {1}'.format(self.type, self.price)

class Desktop(Device):
    pass

class Laptop(Device):
    pass

class Mobile(Device):
    pass
