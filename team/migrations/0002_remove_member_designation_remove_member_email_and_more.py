# Generated by Django 4.2.1 on 2023-07-09 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='designation',
        ),
        migrations.RemoveField(
            model_name='member',
            name='email',
        ),
        migrations.RemoveField(
            model_name='member',
            name='name',
        ),
        migrations.RemoveField(
            model_name='member',
            name='password',
        ),
        migrations.RemoveField(
            model_name='member',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='member',
            name='username',
        ),
    ]
