from django.db import models

from referentiel.models import Individu

# Create your models here.


class Commandes(models.Model):
    individu = models.ManyToManyField(Individu)
    quantité = models.IntegerField()
    ref_article = models.IntegerField()
    



class Cheques(models.Model):
    num_cheque = models.IntegerField()
    nom_banque = models.CharField(max_length=100)

class CB(models.Model):
    num_carte = models.IntegerField()
    date_expiration = models.DateField()