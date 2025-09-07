from django.db import models

# Create your models here.
from django.contrib.auth.models import User



class Task ( models.Model):

    # user = models.ForeignKey( User , on_delete= models.CASCADE , blank= True , null=True)
    title = models.CharField( max_length= 200)
    description = models.TextField( blank= True)
    completed = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.title