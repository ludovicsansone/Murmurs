from django.db import models
from django.contrib.auth.models import User

class Univers(models.Model):
    pseudo = models.CharField(max_length = 30)
    sexe = models.CharField(max_length=6, null = True)
    recherche = models.CharField(max_length=6, null = True)
    dateDeNaissance = models.DateField(auto_now = False, auto_now_add = False, null = True)
    villeDeResidence = models.CharField(max_length=50, null = True)
    status = models.CharField(max_length=10, null = True)
    enLigne = models.BooleanField(null = True)
    presentation = models.TextField(null = True)
    nombreDEnfant = models.SmallIntegerField(null = True)
    presentationVocale = models.FileField(upload_to = 'mediats.sounds', max_length = 100, null = True)
    photo = models.ImageField(upload_to = 'mediats.images', height_field = None, width_field = None, max_length = None, null = True)
    informations = models.SmallIntegerField(default = 0)
    livrePrefere = models.CharField(max_length = 100, null = True)
    aProposDuLivre = models.CharField(max_length=1000, null = True)
    filmPrefere = models.CharField(max_length = 100, null = True)
    aProposDuFilm = models.CharField(max_length=1000, null = True)
    chansonPreferee = models.CharField(max_length = 100, null = True)
    aProposDeLaChanson = models.CharField(max_length=1000, null = True)
    utilisateur = models.OneToOneField(User, verbose_name = "Utilisateur", on_delete = models.CASCADE)

    def __str__(self):
        return self.pseudo
    