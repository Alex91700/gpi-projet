# Generated by Django 3.1.7 on 2021-03-28 17:54

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('referentiel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='referentiel.individu')),
            ],
        ),
        migrations.CreateModel(
            name='Vente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.PositiveIntegerField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='referentiel.article')),
                ('commande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Commandes.commande')),
            ],
        ),
        migrations.CreateModel(
            name='Reglement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField()),
                ('date', models.DateTimeField()),
                ('montant', models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(0)])),
                ('banque', models.CharField(blank=True, max_length=50, null=True)),
                ('date_expiration', models.DateField(blank=True, null=True)),
                ('commande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Commandes.commande')),
            ],
        ),
    ]
