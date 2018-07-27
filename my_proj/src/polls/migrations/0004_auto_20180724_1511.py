# Generated by Django 2.0.4 on 2018-07-24 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_project_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='deadline',
            field=models.DateField(blank=True, null=True, verbose_name='deadline'),
        ),
        migrations.AddField(
            model_name='project',
            name='resolution',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='resolution'),
        ),
        migrations.AddField(
            model_name='project',
            name='startdate',
            field=models.DateField(blank=True, null=True, verbose_name='start date'),
        ),
    ]
