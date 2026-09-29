from django.db import models

# Create your models here.
class Unit(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length= 50)

    def __str__(self):
        return f"{self.code} - {self.name}"
    
