# Generated by Django 3.2.8 on 2021-11-05 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_movie_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ratingstart',
            options={'ordering': ['value']},
        ),
    ]
