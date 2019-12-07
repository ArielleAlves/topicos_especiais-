from django.contrib import admin

# Register your models here

from .models import Estilo, Tipo, Musica

from .models import *

admin.site.register(Estilo)
admin.site.register(Tipo)
admin.site.register(Musica)
