# -*- coding: utf-8 -*-
from django.contrib import admin
from django.forms import ModelForm
from teachers.models import Teacher, School, Employed, State, Education, Diploma, Marriage, State, JobTitle
from mptt.admin import MPTTModelAdmin
import selectable.forms as selectable
from lookups import JobTitleLookup, MarriageLookup, GenderLookup

    
class EmployedInline(admin.TabularInline):
    model = Employed
    extra = 1
    fieldsets = [
        ('Kennsluflokkar',   {'fields': ['school', 'school_type']}), 
        ('Kennslustörf',     {'fields': ['job_type', 'extra_job', 'state_junior_school', 'local_junior_school'], 'classes': ['wide', 'extrapretty']}),
        
]

class EducationInline(admin.TabularInline):
    model = Education
    extra = 1

        
class MarriageAdminForm(ModelForm):
    
    class Meta:
        model = Marriage
        widgets = {
            'marriage_status': selectable.AutoCompleteSelectWidget(lookup_class=MarriageLookup),
        }
        
class MarriageInline(admin.TabularInline):
    model = Marriage
    extra = 1

        
class StateAdmin(MPTTModelAdmin):
    
    class MPTTMeta:
        order_insertion_by = ['name']
        parent_attr = 'parent'

class TeacherAdminForm(ModelForm):

    class Meta:
        model = Teacher
        widgets = {
            'job_mother': selectable.AutoCompleteWidget(lookup_class=JobTitleLookup, allow_new=True),
            'job_father': selectable.AutoComboboxWidget(lookup_class=JobTitleLookup),
            'gender': selectable.AutoCompleteSelectWidget(lookup_class=GenderLookup),
        }

        
class TeacherAdmin(admin.ModelAdmin):
    # This will generate a ModelForm
    inlines = [EmployedInline, EducationInline, MarriageInline]
    list_filter = ['name']
    search_fields = ['name']
    list_display = ['name', 'dob']
    list_editable = ['dob']
   
    
class SchoolAdmin(admin.ModelAdmin):
    model = School    

class DiplomaAdmin(admin.ModelAdmin):
    model = Diploma    

class JobTitleAdmin(admin.ModelAdmin):
    model = JobTitle    



admin.site.register(Teacher, TeacherAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Diploma, DiplomaAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(JobTitle, JobTitleAdmin)