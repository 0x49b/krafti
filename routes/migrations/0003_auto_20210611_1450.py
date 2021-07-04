# Generated by Django 3.2.4 on 2021-06-11 12:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0002_alter_route_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='route',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('5989fc05-a692-4157-a094-39e341061065'), editable=False, null=True),
        ),
    ]