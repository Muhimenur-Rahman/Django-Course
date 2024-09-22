from django.db import models
from catagories.models import catagories_model
from django.contrib.auth.models import User

# Create your models here.

class posts_model(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    catagory = models.ManyToManyField(catagories_model)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
