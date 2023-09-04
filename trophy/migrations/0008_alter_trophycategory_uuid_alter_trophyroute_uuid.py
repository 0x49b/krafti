# Generated by Django 4.2.4 on 2023-09-04 08:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('trophy', '0007_alter_trophycategory_uuid_alter_trophyroute_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trophycategory',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('d0a53dd0-5682-43bf-a82f-a27e0e65b29c'), editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='trophyroute',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('625ab3b9-6777-4df9-ba45-7e07e9ec15d7'), editable=False, null=True),
        ),
    ]
