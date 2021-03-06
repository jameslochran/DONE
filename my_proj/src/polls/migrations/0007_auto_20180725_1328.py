# Generated by Django 2.0.4 on 2018-07-25 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20180724_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='budget',
            field=models.IntegerField(default=0.0, verbose_name='budget'),
        ),
        migrations.AddField(
            model_name='project',
            name='state',
            field=models.CharField(choices=[('To-Do', 'To Do'), ('In Progress', 'In Progress'), ('Blocked', 'Blocked'), ('Done', 'Done'), ('Dismissed', 'Dismissed')], default='to-do', max_length=20, verbose_name='state'),
        ),
    ]
