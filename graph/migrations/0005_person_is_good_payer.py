# Generated by Django 2.0.7 on 2018-07-08 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0004_auto_20180708_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='is_good_payer',
            field=models.BooleanField(default=True),
        ),
    ]
