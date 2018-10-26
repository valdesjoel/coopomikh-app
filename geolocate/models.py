from django.db import models

# Create your models here.


class Etablissement(models.Model):
	nom = models.CharField(max_length=255, null=True, blank=True, verbose_name="Nom de l'Etablissement")
	ville = models.CharField(max_length=255, null=True, verbose_name="Ville")
	quartier = models.CharField(max_length=255, verbose_name="Nom du Quartier")
	repere = models.TextField(max_length=255, verbose_name="Répère")
	telephone = models.CharField(max_length=30, verbose_name="Telephone(s)")
	email = models.EmailField(max_length=255, verbose_name="Email(s)")
	adresse = models.CharField(max_length=255, verbose_name="Adresse")
	latitude = models.CharField(max_length=255, verbose_name="Latitude")
	longitude = models.CharField(max_length=255, verbose_name="Longitude")


	def __str__(self):
		return self.nom


	class Meta:
		verbose_name_plural = "Etablissements"


