# Generated by Django 3.2.4 on 2021-06-20 20:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0005_alter_route_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('ad1c4d6d-fd1b-4588-abce-07c132fff1b0'), editable=False, null=True),
        ),
    ]
