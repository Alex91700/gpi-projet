# Generated by Django 3.1.7 on 2021-04-09 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Anomalies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='anomalie',
            name='courrier',
            field=models.BooleanField(default=False),
        ),
    ]
