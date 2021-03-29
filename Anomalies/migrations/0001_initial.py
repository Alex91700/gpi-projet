# Generated by Django 3.1.7 on 2021-03-29 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Commandes', '0002_commande_valide'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anomalie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Erreur sur le montant', 'Erreur sur le montant'), ('Probleme sur le moyen de paiement', 'Probleme sur le moyen de paiement')], default='Erreur sur le montant', max_length=45)),
                ('date_generation', models.DateField()),
                ('commande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Commandes.commande')),
            ],
        ),
    ]
