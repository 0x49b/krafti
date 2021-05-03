# Generated by Django 3.2 on 2021-05-03 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_loggedin', models.BigIntegerField()),
                ('current_free', models.BigIntegerField()),
                ('added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Visit',
                'verbose_name_plural': 'Visits',
            },
        ),
        migrations.AddIndex(
            model_name='visits',
            index=models.Index(fields=['id', 'added'], name='counter_vis_id_ac7029_idx'),
        ),
    ]
