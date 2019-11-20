from django.db import models

# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length = 100)
	subject = models.CharField(max_length = 100)
	roll_no = models.IntegerField(primary_key=True)

class Marks(models.Model):
	roll_no = models.IntegerField(primary_key=True )
	marks = models.FloatField( default = 0 )