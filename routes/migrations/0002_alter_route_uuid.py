# Generated by Django 3.2.4 on 2021-07-08 08:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('b7991121-c94c-4a53-b039-e8e352db0390'), editable=False, null=True),
        ),
    ]
