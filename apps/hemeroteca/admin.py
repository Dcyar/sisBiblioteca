from django.contrib import admin
from .models import Articulo, Revista
# Register your models here.

class modelArtRev(admin.ModelAdmin):
	list_display = ('titulo', 'autor', 'url', 'fechaPublicacion',)


admin.site.register(Articulo, modelArtRev)
admin.site.register(Revista, modelArtRev)