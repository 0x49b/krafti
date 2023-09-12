# Generated by Django 4.2.4 on 2023-09-04 08:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('trophy', '0006_alter_trophycategory_uuid_alter_trophyroute_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trophycategory',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('f5977c7f-3106-4542-86b5-6418bd3e5c4b'), editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='trophyroute',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('1bdb24e1-0780-47e3-af7f-cf4a815bdca4'), editable=False, null=True),
        ),
    ]