from django.db import models

class Cliente(models.Model):
    #Mostrar cuando creamos un cliente
    created_at = models.DateTimeField(auto_now_add=True)
    #Todos los atributos de nuestro formulario
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    pais = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=20)
    numero = models.CharField(max_length=20)
    correo = models.CharField(max_length=100)
    
    def __str__(self):
        return(f"{self.nombre} {self.apellido} ")
#{self.pais} {self.ciudad} {self.numero} {self.correo}
