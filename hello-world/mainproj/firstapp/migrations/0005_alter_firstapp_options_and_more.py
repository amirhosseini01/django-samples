# Generated by Django 4.1.4 on 2023-01-19 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('firstapp', '0004_firstapp_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='firstapp',
            options={'ordering': ['createAt']},
        ),
        migrations.AlterUniqueTogether(
            name='firstapp',
            unique_together={('owner', 'link')},
        ),
    ]
