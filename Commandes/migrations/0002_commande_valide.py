# Generated by Django 3.1.7 on 2021-03-29 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Commandes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='valide',
            field=models.BooleanField(default=False),
        ),
    ]