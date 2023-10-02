from django.db import models

# Create your models here.
class Assignment(models.Model):
    #currently just basic info, flesh out as needed
    title = models.CharField(max_length=225)
    description = models.TextField(blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    #assigned_to is currently just text, will later connect to users/employees table
    assigned_to = models.CharField(max_length=225, blank=True, default='')

    def __str__(self):
        return f"{self.title}"
