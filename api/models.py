from django.db import models

# Create your models here.
class  student(models.Model):
    name= models.CharField(max_length=20)
    rollno= models.IntegerField(primary_key=True)
    def __str__(self):
        return self.name +" "+ str(self.rollno)