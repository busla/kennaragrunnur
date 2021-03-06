# -*- coding: utf-8 -*-
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Diploma(models.Model):
    name = models.CharField('Prófgráða', max_length=255)

    def __unicode__(self):
        return self.name

class JobTitle(models.Model):
    job_id = models.IntegerField('Kóði', unique=True)    
    name = models.CharField('Starfsheiti', max_length=255)

    def __unicode__(self):
        return self.name

class State(MPTTModel):
    name = models.CharField(max_length=150, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='county')

    def __unicode__(self):
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
    dob = models.DateField('Fæðingarár', null=True, blank=True)
    deceased = models.DateField('Dánarár', null=True, blank=True)
    birthplace = TreeForeignKey(State, related_name='birthplace', null=True, blank=True, )
    children_related = models.IntegerField('Fjöldi skyldra barna', null=True, blank=True)
    children_foster = models.IntegerField('Fjöldi fósturbarna', null=True, blank=True)
    children_adopted = models.IntegerField('Fjöldi kjörbarna', null=True, blank=True)
    dob_youngest_child = models.DateField('Fæðingarár yngsta barns', null=True, blank=True)
    dob_oldest_child = models.DateField('Fæðingarár elsta barns', null=True, blank=True)
    job_mother = models.ForeignKey(JobTitle, related_name='job_mother', null=True, blank=True)
    job_father = models.ForeignKey(JobTitle, related_name='job_father', null=True, blank=True)    
    teaching_started = models.DateField('Upphaf kennslu', null=True, blank=True)
    teaching_ended = models.DateField('Lok kennslu', null=True, blank=True)
    
    
    def __unicode__(self):
        return self.name

class School(models.Model):
    name = models.CharField('Heiti', max_length=255)
    area = TreeForeignKey(State, related_name='area')
    teacher = models.ManyToManyField(Teacher, through='Employed')

    def __unicode__(self):
        return self.name
        
class Employed(models.Model):
    JOB_TYPE_CHOICES = (
        (1, 'Fastráðinn'),
        (2, 'Stundakennari'),
    )

    SCHOOL_TYPE_CHOICES = (
        (1, 'Fastur skóli'),
        (2, 'Heimavist'),
        (3, 'Farskóli'),
        (4, 'Eftirlitskennsla'),
    )

    BOOLEAN_CHOICES = (
        (0, 'Nei'),
        (1, 'Já'),
    )

    teacher = models.ForeignKey(Teacher)
    school = models.ForeignKey(School)
    year = models.DateField('Starfsár')
    job_type = models.IntegerField('Kennslustaða', choices=JOB_TYPE_CHOICES)
    extra_job = models.ForeignKey(JobTitle)
    school_type = models.IntegerField('Tegund skóla', choices=SCHOOL_TYPE_CHOICES)
    state_junior_school = models.IntegerField('Héraðsgagnfræðikennari', choices=BOOLEAN_CHOICES, default=0)
    local_junior_school = models.IntegerField('Gagnfræðikennari', choices=BOOLEAN_CHOICES, default=0)
    elementary_school = models.IntegerField('Barnaskólakennari', choices=BOOLEAN_CHOICES, default=1)
    gastronomy_school = models.IntegerField('Matreiðslukennari', choices=BOOLEAN_CHOICES, default=0)
    has_certificate = models.IntegerField('Hefur kennsluréttindi', choices=BOOLEAN_CHOICES, default=0)


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
        (7, 'Makamissir'),        
    )

    teacher = models.ForeignKey(Teacher)
    marriage_status = models.IntegerField('Hjúskapur', choices=MARRIAGE_CHOICES, default=1)
    year = models.DateField('Ár')