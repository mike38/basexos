from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager

# Create your models here.

class Exercice(models.Model):
    titre = models.CharField(max_length=255) 
    classe = models.CharField(max_length=20)
    matiere = models.CharField(max_length=255)
    chapitre = models.CharField(max_length=255)
    motclef = TaggableManager()
    origine = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)


class Files(models.Model):
    id_ex = models.ForeignKey(Exercice)
    fichier = models.FileField(upload_to='Fichiers')
    format_fichier = models.CharField(max_length=255)
    date_ajout = models.DateField(auto_now_add=True) 
    version = models.PositiveSmallIntegerField()
    correction = models.BooleanField(default=False)

class Test_files(models.Model):
    fichier = models.FileField(upload_to=settings.MEDIA_ROOT)
    
