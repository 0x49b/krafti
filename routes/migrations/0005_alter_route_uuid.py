# Generated by Django 3.2.4 on 2021-06-20 20:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0004_auto_20210611_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('2205f8bb-fa66-465a-b24b-de1b6525d659'), editable=False, null=True),
        ),
    ]
