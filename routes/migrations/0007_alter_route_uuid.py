# Generated by Django 3.2.4 on 2021-06-20 20:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0006_alter_route_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('3a70ad31-8830-403c-8647-d0b817c03ceb'), editable=False, null=True),
        ),
    ]