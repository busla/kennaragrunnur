# -*- coding: utf-8 -*-
from django.db import models

class State(models.Model):
    state_id = models.IntegerField('Kóði', unique=True)
    name = models.CharField('Heiti', max_length=255)

    def __str__(self):
        return self.name

class Area(models.Model):
    area_id = models.IntegerField('Kóði', unique=True)
    name = models.CharField('Heiti', max_length=255)
    state = models.ForeignKey(State)

    def __str__(self):
        return self.name

class Diploma(models.Model):
    name = models.CharField('Prófgráða', max_length=255)

    def __str__(self):
        return self.name
         
class Teacher(models.Model):
    GENDER_CHOICES = (
        (0, 'Karl'),
        (1, 'Kona'),
        (3, 'Þriðja kynið'),
        (4, 'Óþekkt'),
    )
    
    name = models.CharField('Nafn', max_length=255)
    gender = models.IntegerField('Kyn', choices=GENDER_CHOICES, default=0)
    dob = models.DateField('Fæðingarár')
    deceased = models.DateField('Dánarár')
    birthplace = models.ForeignKey(Area)
    children_related = models.IntegerField('Fjöldi skyldra barna', blank=True)
    children_foster = models.IntegerField('Fjöldi fósturbarna', blank=True)
    children_adopted = models.IntegerField('Fjöldi kjörbarna', blank=True)
    dob_youngest_child = models.DateField('Fæðingarár yngsta barns', blank=True)
    dob_oldest_child = models.DateField('Fæðingarár elsta barns', blank=True)
    
    def __str__(self):
        return self.name

class School(models.Model):
    name = models.CharField('Heiti', max_length=255)
    area = models.ForeignKey(Area)
    teacher = models.ManyToManyField(Teacher, through='Employed')

    def __str__(self):
        return self.name
        
class Employed(models.Model):
    teacher = models.ForeignKey(Teacher)
    School = models.ForeignKey(School)
    year = models.DateField('Starfsár')

class Education(models.Model):
    teacher = models.ForeignKey(Teacher)
    year = models.DateField('Próftökuár')
    diploma = models.ForeignKey(Diploma)

class Marriage(models.Model):
    MARRIAGE_CHOICES = (
        (1, 'Ógift/ur'),
        (3, 'Gift/ur'),
        (4, 'Ekkill/Ekkja'),
        (6, 'Fráskilin/n'),
    )
    
    teacher = models.ForeignKey(Teacher)
    marriage_status = models.IntegerField('Hjúskapur', choices=MARRIAGE_CHOICES, default=1)
    year = models.DateField('Hjúskaparár')
    
