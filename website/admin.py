from django.contrib import admin
from .models import Cliente

#Para que le permita el admin añadir cliente
admin.site.register(Cliente)

