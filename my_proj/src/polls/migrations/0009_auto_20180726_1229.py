# Generated by Django 2.0.4 on 2018-07-26 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20180725_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='state',
            field=models.CharField(choices=[('To-Do', 'To Do'), ('In Progress', 'In Progress'), ('Blocked', 'Blocked'), ('Done', 'Done'), ('Dismissed', 'Dismissed')], default='To Do', max_length=20, verbose_name='state'),
        ),
    ]