from django.db import models

# Create your models here.


class Commandes(models.Model):
    individu = models.ManyToManyField(Individu)
    quantité = models.Integer(max_digits = 5)
    ref_article = models.Integer(max_digits = 15)
    type_reglement = models.ForeignKey(Reglement, on_delete=models.CASCADE)

class Reglement(models.Model):
    cb = models.ForeignKey(CB, on_delete=models.CASCADE)
    cheque = models.ForeignKey(Cheques, on_delete=models.CASCADE)

class Cheques(models.Model):
    num_cheque = models.Integer(max_digits=10)
    nom_banque = models.CharField(max_length=100)

class CB(models.Model):
    num_carte = models.IntegerField(max_digits=10)
    date_expiration = models.DateField()