from django.db import models


class Especie(models.Model):
    n_comun = models.TextField(max_length=128, verbose_name="Nombre Comun")
    n_cientifico = models.TextField(
        max_length=128,  verbose_name="Nombre Cientifico")
    familia = models.TextField(max_length=128,  verbose_name="Familia")

    class Meta:
        verbose_name = "Especie"
        verbose_name_plural = "Especies"
        ordering = ["-pk"]

    def get_Esp(self):
        return str("{}".format(self.n_comun))

    def __str__(self):
        return self.n_comun


class Lugar(models.Model):
    pais = models.CharField(max_length=128,  verbose_name="Pais")
    departamento = models.CharField(
        max_length=128, verbose_name="Departamento")
    nombre = models.CharField(max_length=128,  verbose_name="Nombre")
    alias = models.CharField(max_length=128,  verbose_name="Alias")

    class Meta:
        verbose_name = "Lugar"
        verbose_name_plural = "Lugares"
        ordering = ["-pk"]

    def __str__(self):
        return self.nombre


class Avistamiento(models.Model):
    latitud = models.FloatField(verbose_name="Latitud")
    longitud = models.FloatField(verbose_name="Longitud")
    autor = models.CharField(max_length=128,  verbose_name="Autor")
    observación = models.TextField(
        null=True, blank=True, verbose_name="Observaciones")
    especie = models.ManyToManyField(Especie)
    lugar = models.ForeignKey(
        Lugar, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Avistamiento"
        verbose_name_plural = "Avistamientos"
        ordering = ["-pk"]

    def __str__(self):
        return 'ID={},Autor={}'.format(self.pk, self.autor)
