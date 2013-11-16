from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=255)
    gender = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
        
class School(models.Model):
    name = models.CharField(max_length=255)
    teacher = models.ManyToManyField(Teacher, through='Employed')

    def __str__(self):
        return self.name
        
class Employed(models.Model):
    teacher = models.ForeignKey(Teacher)
    School = models.ForeignKey(School)
    year = models.DateField()
    