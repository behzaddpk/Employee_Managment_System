# Generated by Django 4.2.1 on 2023-07-14 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminModule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='Designate',
            field=models.CharField(choices=[('1', 'ADMIN'), ('2', 'PARTNER'), ('3', 'CORDINATOR'), ('4', 'TEAM LEADER'), ('5', 'WRITER'), ('6', 'MEMBER')], default=1, max_length=50),
        ),
    ]
