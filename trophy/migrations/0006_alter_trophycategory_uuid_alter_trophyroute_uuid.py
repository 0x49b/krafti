# Generated by Django 4.2.4 on 2023-09-01 06:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('trophy', '0005_alter_trophycategory_uuid_alter_trophyroute_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trophycategory',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('82fd9dfa-9c8b-4854-a027-c9694417e786'), editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='trophyroute',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('3a67b11a-5a9b-4151-9274-2816972527f8'), editable=False, null=True),
        ),
    ]
