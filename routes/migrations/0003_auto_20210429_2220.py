# Generated by Django 3.1.4 on 2021-04-29 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0002_route_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='categorie',
            field=models.IntegerField(choices=[(0, 'Galerie Vorstieg'), (1, 'Turm Toprope'), (2, 'Turm Vorstieg'), (3, 'Hauptwand'), (4, 'Galerie Toprope')]),
        ),
    ]
