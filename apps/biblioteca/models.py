from django.db import models

# Create your models here.

class Autor(models.Model):
	nombre    = models.CharField(max_length = 30, unique = True)
	apellido  = models.CharField(max_length = 30)
	pais	  = models.CharField(max_length = 30)
	biografia = models.URLField()

	def __str__(self):
		return "%s %s" % (self.nombre , self.apellido)


class Editorial(models.Model):
	nombre 	  = models.CharField(max_length = 30, unique = True)
	direccion = models.CharField(max_length = 30)
	telefono  = models.CharField(max_length = 9)
	correo 	  = models.EmailField()
	pais	  = models.CharField(max_length = 20)

	def __str__(self):
		return self.nombre


class Carrera(models.Model):
	carrera = models.CharField(max_length = 30, unique = True)

	def __str__(self):
		return self.carrera


class Libro(models.Model):
	titulo 			 = models.CharField(max_length = 50, unique = True)
	fechaPublicacion = models.CharField(max_length = 30)
	edicion 		 = models.CharField(max_length = 50)
	area			 = models.CharField(max_length = 50)
	imagen			 = models.ImageField(upload_to = 'libro')
	stock			 = models.PositiveIntegerField()
	estado 			 = models.BooleanField(default = True)

	autor 	  = models.ForeignKey(Autor)
	editorial = models.ForeignKey(Editorial)
	carrera   = models.ForeignKey(Carrera)

	def __str__(self):
		return self.titulo


class Estudiante(models.Model):
	nombre 	   = models.CharField(max_length = 30)
	apellido   = models.CharField(max_length = 30)
	celular    = models.CharField(max_length = 9)
	dni 	   = models.CharField(max_length = 8)
	sexo	   = models.CharField(max_length = 1)
	direccion  = models.CharField(max_length = 50)
	correo	   = models.EmailField()
	fecIngreso = models.CharField(max_length = 10)
	estado	   = models.BooleanField(default = True)
	prestamos   = models.BooleanField(default = False)

	carrera = models.ForeignKey(Carrera)

	def __str__(self):
		return "%s %s" % (self.nombre , self.apellido)


class Reserva(models.Model):
	reserva 	 = models.CharField(max_length = 8, unique = True)
	fechaReserva = models.DateTimeField(auto_now_add = True)
	estado 		 = models.BooleanField(default = True)

	libro  = models.ForeignKey(Libro)
	estudiante = models.ForeignKey(Estudiante)

	def __str__(self):
		return self.reserva

class Prestamo(models.Model):
	fechaPrestamo   = models.DateTimeField(auto_now_add = True, auto_now = False)
	fechaDevolucion = models.DateTimeField(blank = True, null = True)
	estado 			= models.BooleanField(default = True)

	libro 	   = models.ForeignKey(Libro)
	estudiante = models.ForeignKey(Estudiante)

	def __unicode__(self):
		return self.estudiante