from django.contrib import admin
from exercices.models import Exercice, Files, Test_files

# Register your models here.

admin.site.register(Exercice)
admin.site.register(Test_files)

#class ExerciceAdmin(admin.ModelAdmin):
    

