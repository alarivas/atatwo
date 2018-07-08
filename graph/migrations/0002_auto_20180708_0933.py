# Generated by Django 2.0.7 on 2018-07-08 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='relation',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
