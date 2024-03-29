# Generated by Django 4.2.1 on 2023-07-12 04:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('team', '0002_remove_member_designation_remove_member_email_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_token', models.CharField(blank=True, max_length=100, null=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=True)),
                ('team_captain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.team')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Writer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WriterSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=255)),
                ('Writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='writer.writer')),
            ],
        ),
        migrations.CreateModel(
            name='WriterProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_no', models.CharField(max_length=11)),
                ('tag', models.CharField(max_length=255, null=True)),
                ('address', models.CharField(max_length=255)),
                ('Writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='writer.writer')),
            ],
        ),
        migrations.CreateModel(
            name='WriterPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='Writer')),
                ('Writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='writer.writer')),
            ],
        ),
        migrations.CreateModel(
            name='WriterExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ExperiencedField', models.CharField(max_length=255)),
                ('ExperiencedYear', models.DecimalField(decimal_places=2, max_digits=3)),
                ('Writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='writer.writer')),
            ],
        ),
        migrations.CreateModel(
            name='WriterEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudyIn', models.CharField(max_length=255)),
                ('PassingYear', models.DateField()),
                ('Writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='writer.writer')),
            ],
        ),
        migrations.CreateModel(
            name='WriterBio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', tinymce.models.HTMLField()),
                ('Writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='writer.writer')),
            ],
        ),
        migrations.CreateModel(
            name='BankDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BankName', models.CharField(choices=[('ABP', 'Al Baraka Bank (Pakistan) Limited'), ('ABL', 'Allied Bank Limited'), ('AB', 'Askari Bank'), ('BAP', 'Bank Alfalah Limited'), ('BAH', 'Bank Al-Habib Limited'), ('BIP', 'BankIslami Pakistan Limited'), ('BOP', 'Bank of Punjab'), ('FBL', 'Faysal Bank Limited'), ('HBL', 'Habib Bank Limited'), ('JS', 'JS Bank Limited'), ('MCB', 'MCB Bank Limited'), ('MBL', 'Meezan Bank Limited'), ('NBP', 'National Bank of Pakistan'), ('SB', 'Summit Bank Pakistan'), ('UBL', 'United Bank Limited (UBL)')], max_length=255)),
                ('AccountNO', models.IntegerField()),
                ('Writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='writer.writer')),
            ],
        ),
    ]
