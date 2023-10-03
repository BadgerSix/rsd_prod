from django.db import models

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=225)
    lastname = models.CharField(max_length=225)
    job_title = models.CharField(max_length=225, default='Team Member')
    date_joined = models.DateField(null=True)
    phone = models.BigIntegerField(null=True)
    email = models.EmailField(max_length=225, blank=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
