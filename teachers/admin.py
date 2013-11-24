from django.contrib import admin
from teachers.models import Teacher, School, Employed, Area, State, Education, Diploma, Marriage, Genre
from mptt.admin import MPTTModelAdmin

class EmployedInline(admin.TabularInline):
    model = Employed
    extra = 1

class EducationInline(admin.TabularInline):
    model = Education
    extra = 1

class MarriageInline(admin.TabularInline):
    model = Marriage
    extra = 1

class GenreAdmin(MPTTModelAdmin):
    
    class MPTTMeta:
        order_insertion_by = ['name']
        parent_attr = 'parent'
        
        
class TeacherAdmin(admin.ModelAdmin):
    inlines = [EmployedInline, EducationInline, MarriageInline]
    list_filter = ['name']
    search_fields = ['name']
    
class AreaAdmin(admin.ModelAdmin):
    model = Area

class StateAdmin(admin.ModelAdmin):
    model = State    

class SchoolAdmin(admin.ModelAdmin):
    model = School    

class DiplomaAdmin(admin.ModelAdmin):
    model = Diploma    
        
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Diploma, DiplomaAdmin)
admin.site.register(Genre, GenreAdmin)