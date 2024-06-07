from django.db import models

class Entite(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50, blank=True)
    adresse = models.CharField(max_length=200, blank=True)
    code_postal = models.CharField(max_length=8, blank=True)
    ville = models.CharField(max_length=50, blank=True)
    telephone_fixe = models.CharField(max_length=20, blank=True)
    telephone_portable = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    date_naissance = models.DateField(null=True, blank=True)
    note = models.TextField(blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
