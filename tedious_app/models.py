from django.db import models

# Create your models here.
class Task(models.Model):
    description = models.CharField(max_length=50)
    time = models.IntegerField(default=0)
    person = models.CharField(max_length=50)
    
    def __str__(self):
        return self.person

    def get_absolute_url(self):
        return "/home/"