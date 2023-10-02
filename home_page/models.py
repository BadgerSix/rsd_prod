from django.db import models

# Create your models here.
class App(models.Model):
    name = models.CharField(max_length=225)
    url_main = models.CharField(max_length=225, default='/')

    def __str__(self):
        return f"{self.name}"