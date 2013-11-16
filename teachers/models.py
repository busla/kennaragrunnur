from django.db import models

class Teacher(models.Model):
    GENDER_CHOICES = (
        (0, 'Karl'),
        (1, 'Kona'),
        (3, 'Þriðja kynið'),
        (4, 'Óþekkt'),
    )
    
    name = models.CharField(max_length=255)
    gender = models.IntegerField(choices=GENDER_CHOICES, default=0)
    dob = models.DateField()
    deceased = models.DateField()
    
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
    
class Area(models.Model):
    area_id = models.IntegerField(unique=True)