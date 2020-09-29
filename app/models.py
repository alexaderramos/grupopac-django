from django.db import models


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f'Cliente: {self.id} {self.name}, {self.email}'
