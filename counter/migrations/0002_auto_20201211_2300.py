# Generated by Django 3.1.4 on 2020-12-11 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visits',
            name='added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]