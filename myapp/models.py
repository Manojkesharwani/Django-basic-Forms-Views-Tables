from django.db import models
from datetime import datetime

# Create your models here.
class project(models.Model):
    name=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    salary=models.IntegerField(null=True)
    date=models.DateField(default=datetime.now)

    def __str__(self):
        return self.name