from django.db import models
from django.contrib import admin
from django.forms import ModelForm
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver


class Portfolio(models.Model):
    nombre = models.CharField(max_length=70,null=True)
    image = models.ImageField(upload_to='static/imagenPortfolio')

    def __str__(self):
        return self.nombre
    class Meta:
         verbose_name = "1) Portfolio (vertical)."
    
  

class Albume(models.Model):
    albume_fields = models.ImageField(upload_to='static/imgenesportada')
    nombre = models.CharField(max_length=21,null=True)
    fecha = models.DateField()
    comentario = models.CharField(max_length=500,null=True)
    albumDestacado = models.BooleanField(default=False)
    fkPortFolio = models.ForeignKey(Portfolio, on_delete = models.CASCADE, null= True)


    def __str__(self):
        return self.nombre
    class Meta:
         verbose_name = "2) Album (horizontal)."

class ImgAlbume(models.Model): 
    image = models.ImageField(upload_to='static/imagenesalbum')
    fkAlbume = models.ForeignKey(Albume, on_delete = models.CASCADE, null= True)

    class Meta:
         verbose_name = "3) Img de los Album"

class PortfolioSoloImg(models.Model):
    nombre = models.CharField(max_length=70,null=True)
    image = models.ImageField(upload_to='static/imagenPortfolio')

    def __str__(self):
        return self.nombre

    class Meta:
         verbose_name = "4) Portfolio sin album (vertical)"


class SoloImg(models.Model):
    image = models.ImageField(upload_to='static/imagenesalbum')
    fkPortfolioSoloImg= models.ForeignKey(PortfolioSoloImg, on_delete = models.CASCADE, null= True)
    
    class Meta:
         verbose_name = "5) Img sin album"
    
   
     
class Contacto(models.Model):
    
    nombre = models.CharField(max_length=500,null=True)
    email = models.EmailField(max_length=254, null=True)
    telefono = models.IntegerField(null=True)
    respuesta1 = models.CharField(max_length=500,null=True)
    respuesta2 = models.CharField(max_length=500,null=True)
    respuesta3 = models.CharField(max_length=500,null=True)
    respuesta4 = models.CharField(max_length=500,null=True)
    respuesta5 = models.CharField(max_length=500,null=True,blank=True)

    def __str__(self):
        return self.nombre
    class Meta:
         verbose_name = "7) Contacto"


class Pack(models.Model):

    nombre = models.CharField(max_length=500,null=True, blank=True)
    pack_fields = models.ImageField(upload_to='static/packs',blank=True)
    descripcion= models.TextField(max_length=900, null=True, blank=True)

    def __str__(self):
        return str(self.nombre) if self.nombre else 'No le adjudicaron un nombre'

    class Meta:
         verbose_name = "6) Pack"