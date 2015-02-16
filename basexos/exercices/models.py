from django.db import models

# Create your models here.

class Exercice(models.Model):
    titre = models.CharField(max_length=255) 
    classe = models.CharField(max_length=20)
    matiere = models.CharField(max_length=255)
    chapitre = models.CharField(max_length=255)
#    mot_clef = django-taggit 
    origine = models.CharField(max_length=255)


class files(models.Model):
    id_ex = models.ForeignKey(Exercice)
    fichier = models.FileField(upload_to='Fichiers')
    format = models.CharField(max_length=255)
    date_ajout = models.DateField(auto_now_add=True) 
    version = models.PositiveSmallIntegerField()
    type = models.CharField(max_length=255)

