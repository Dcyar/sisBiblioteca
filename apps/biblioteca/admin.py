from django.contrib import admin
from .models import Autor, Editorial, Libro, Estudiante, Carrera, Reserva, Prestamo

# Register your models here.

class modelAutor(admin.ModelAdmin):
	list_display = ('nombre', 'apellido', 'pais',)
	list_filter = ('pais',)


class modelEditorial(admin.ModelAdmin):
	list_display = ('nombre', 'direccion', 'telefono', 'correo', 'pais',)
	list_filter = ('pais',)
	

class modelLibro(admin.ModelAdmin):
	list_display = ('titulo', 'autor', 'editorial', 'fechaPublicacion', 'edicion', 'area', 'imagen', 'estado',)
	list_filter = ('autor', 'editorial', 'area')
	list_editable = ('estado',)
	search_fields = ('titulo', 'autor__nombre',)
	raw_id_fields = ('autor',)


class modelEstudiante(admin.ModelAdmin):
	list_display = ('nombre', 'apellido', 'carrera','celular', 'dni', 'sexo', 'direccion', 'fecIngreso', 'reservas', 'prestamos', )
	list_filter = ('carrera', 'fecIngreso', 'sexo',)
	search_fields = ('apellido',)
	raw_id_fields = ('carrera',)


class modelCarrera(admin.ModelAdmin):
	list_display = ('carrera', )


class modelReserva(admin.ModelAdmin):
	list_display = ('id', 'reserva', 'libro', 'estudiante', 'fechaReserva', 'estado',)
	list_filter = ('libro', 'fechaReserva',)
	search_fields = ('estudiante__nombre', 'estudiante__apellido','libro__titulo')
	raw_id_fields = ('libro', 'estudiante',)


class modelPrestamo(admin.ModelAdmin):
	list_display = ('id', 'estudiante', 'libro', 'fechaPrestamo', 'fechaDevolucion', 'estado',)
	list_filter = ('estudiante', 'libro', 'fechaPrestamo', 'estado',)
	search_fields = ('estudiante__nombre', 'estudiante__apellido','libro__titulo')
	raw_id_fields = ('libro', 'estudiante',)


admin.site.register(Autor, modelAutor)
admin.site.register(Editorial, modelEditorial)
admin.site.register(Libro, modelLibro)
admin.site.register(Estudiante, modelEstudiante)
admin.site.register(Carrera, modelCarrera)
admin.site.register(Reserva, modelReserva)
admin.site.register(Prestamo, modelPrestamo)