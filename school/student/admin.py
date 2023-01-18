from django.contrib import admin
from.models import Student,Class

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name','age','class_id')

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('id','name','description')
