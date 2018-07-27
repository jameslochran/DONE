# Generated by Django 2.0.4 on 2018-07-25 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20180725_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='state',
            field=models.CharField(choices=[('To-Do', 'To Do'), ('In Progress', 'In Progress'), ('Blocked', 'Blocked'), ('Done', 'Done'), ('Dismissed', 'Dismissed')], default='to_do', max_length=20, verbose_name='state'),
        ),
    ]