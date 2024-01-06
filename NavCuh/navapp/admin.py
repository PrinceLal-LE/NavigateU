from django.contrib import admin
from .models import Department,Teacher,School
# Register your models here.

class SchoolAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slugy": ("school_name",)}

class DeptartmentAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("dept_name",)}
    
admin.site.register(School, SchoolAdmin)
admin.site.register(Department, DeptartmentAdmin)
admin.site.register(Teacher)
