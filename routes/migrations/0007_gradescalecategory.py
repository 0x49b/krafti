# Generated by Django 3.2 on 2021-06-03 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0006_auto_20210603_2111'),
    ]

    operations = [
        migrations.CreateModel(
            name='GradeScaleCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Grad Skala Kategorie',
                'verbose_name_plural': 'Grad Skala Kategorien',
            },
        ),
    ]
