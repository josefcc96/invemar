from django.db import models



class Especie(models.Model):
    n_comun = models.TextField(max_length=128)
    n_cientifico = models.TextField(max_length=128)
    familia = models.TextField(max_length=128)

    def __str__(self):
        return self.n_comun


class Lugar(models.Model):
    pais = models.CharField(max_length=128)
    departamento = models.CharField(max_length=128)
    nombre = models.CharField(max_length=128)
    alias = models.CharField(max_length=128)
   

    def __str__(self):
        return self.nombre

  

class Avistamiento(models.Model):
    
    latitud = models.FloatField()
    longitud = models.FloatField()
    autor = models.CharField(max_length=128)
    observación = models.TextField(null=True,blank=True)
    especie = models.ManyToManyField(Especie)
    lugar = models.ForeignKey(Lugar,null=True,blank=True,on_delete=models.CASCADE) 
    
    def __str__(self):
        return 'ID={},Autor={}'.format(self.pk, self.autor)