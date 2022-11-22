from django.contrib import admin
from .models import Ingreso, Gasto, Billetera, Categoria

admin.site.register(Ingreso)
admin.site.register(Gasto)
admin.site.register(Billetera)
admin.site.register(Categoria)