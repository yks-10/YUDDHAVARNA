from django.db import models

class Register(models.Model):
    name = models.CharField(max_length=50)
    college = models.CharField(max_length=100)
    department = models.CharField(max_length=40)
    email = models.EmailField(unique=True, primary_key=True)
    number = models.CharField(max_length=10)
    def __str__(self):
        return self.name

