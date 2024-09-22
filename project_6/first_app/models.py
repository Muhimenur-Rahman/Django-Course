from django.db import models

# Create your models here.

class student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField(primary_key=True)
    address = models.TextField()
    
    def __str__(self) -> str:
        return f"Roll : {self.roll} ,{self.name}"

