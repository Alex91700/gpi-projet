from django.contrib import admin

from .models import Commandes, Cheques, CB
# Register your models here.

aCommandes = [Commandes, Cheques, CB]
admin.site.register(aCommandes)
