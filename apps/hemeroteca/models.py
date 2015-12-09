from django.db import models

# Create your models here.
class Articulo(models.Model):
	titulo 			 = models.CharField(max_length = 30, unique = True)
	autor  			 = models.CharField(max_length = 30)
	url	   			 = models.URLField()
	fechaPublicacion = models.DateField()

	def __str__(self):
		return self.titulo


class Revista(models.Model):
	titulo 			 = models.CharField(max_length = 30, unique = True)
	autor  			 = models.CharField(max_length = 30)
	url	   			 = models.URLField()
	fechaPublicacion = models.DateField()

	def __str__(self):
		return self.titulo