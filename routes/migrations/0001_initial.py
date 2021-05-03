# Generated by Django 3.2 on 2021-05-03 13:06

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Kategorie',
                'verbose_name_plural': 'Kategorien',
            },
        ),
        migrations.CreateModel(
            name='GradeScale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yds', models.CharField(blank=True, max_length=10, null=True, verbose_name='YDS (USA)')),
                ('british_tech', models.CharField(blank=True, max_length=10, null=True, verbose_name='British (UK) Tech')),
                ('british_adj', models.CharField(blank=True, max_length=10, null=True, verbose_name='British (UK) Adj')),
                ('french', models.CharField(blank=True, max_length=10, null=True, verbose_name='Französisch')),
                ('uiaa', models.CharField(blank=True, max_length=10, null=True, verbose_name='UIAA (MiddleEurope)')),
                ('australia', models.CharField(blank=True, max_length=10, null=True, verbose_name='Australia')),
                ('saxon', models.CharField(blank=True, max_length=10, null=True, verbose_name='Sächisch (Sachsen/Nordböhmen)')),
                ('scandinavia', models.CharField(blank=True, max_length=10, null=True, verbose_name='Scandinavia')),
                ('brasil', models.CharField(blank=True, max_length=10, null=True, verbose_name='Brasil')),
                ('fontainebleu', models.CharField(blank=True, max_length=10, null=True, verbose_name='Fontainebleu')),
            ],
            options={
                'verbose_name': 'Grad Skala',
                'verbose_name_plural': 'Grad Skalas',
            },
        ),
        migrations.CreateModel(
            name='RouteArchive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(max_length=3)),
                ('color', colorfield.fields.ColorField(default='#FFFFFF', max_length=18)),
                ('name', models.CharField(max_length=250, unique=True)),
                ('setter', models.CharField(max_length=25)),
                ('date', models.DateField()),
                ('length', models.IntegerField()),
                ('route_num', models.CharField(max_length=4)),
                ('archived', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='routes.category')),
                ('grd', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='routes.gradescale')),
            ],
            options={
                'verbose_name': '[Archiv] Route',
                'verbose_name_plural': '[Archiv] Routen',
            },
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(max_length=3)),
                ('color', colorfield.fields.ColorField(default='#FFFFFF', max_length=18)),
                ('name', models.CharField(max_length=250, unique=True)),
                ('setter', models.CharField(max_length=25)),
                ('date', models.DateField()),
                ('length', models.IntegerField()),
                ('route_num', models.CharField(max_length=4)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='routes.category')),
                ('grd', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='routes.gradescale')),
            ],
            options={
                'verbose_name': 'Route',
                'verbose_name_plural': 'Routen',
            },
        ),
    ]
