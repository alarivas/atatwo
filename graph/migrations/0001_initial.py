# Generated by Django 2.0.7 on 2018-07-08 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('rut', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('person_one', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='person_one', to='graph.Person')),
                ('person_two', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='person_two', to='graph.Person')),
            ],
        ),
    ]
