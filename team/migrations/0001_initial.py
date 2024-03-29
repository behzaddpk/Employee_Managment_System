# Generated by Django 4.2.1 on 2023-07-09 09:07

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('auth_token', models.CharField(max_length=100)),
                ('is_varified', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('password', models.CharField(max_length=50)),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.designation')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MemberSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=255)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.member')),
            ],
        ),
        migrations.CreateModel(
            name='MemberProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_no', models.CharField(max_length=11)),
                ('tag', models.CharField(max_length=255, null=True)),
                ('address', models.CharField(max_length=255)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.member')),
            ],
        ),
        migrations.CreateModel(
            name='MemberPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='Partner')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.member')),
            ],
        ),
        migrations.CreateModel(
            name='MemberExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ExperiencedField', models.CharField(max_length=255)),
                ('ExperiencedYear', models.DecimalField(decimal_places=2, max_digits=3)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.member')),
            ],
        ),
        migrations.CreateModel(
            name='MemberEvaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Monthevaluate', models.DateField()),
                ('Punctuality', models.FloatField(max_length=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('Attitude', models.FloatField(max_length=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('Performance', models.FloatField(max_length=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('Utilities', models.FloatField(max_length=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('Formatiing', models.FloatField(max_length=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('Quality', models.FloatField(max_length=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('Expertise', models.FloatField(max_length=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('New_Learning', models.FloatField(max_length=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('Planning', models.FloatField(max_length=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('AI_Flowed', models.FloatField(max_length=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.member')),
            ],
        ),
        migrations.CreateModel(
            name='MemberEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudyIn', models.CharField(max_length=255)),
                ('PassingYear', models.DateField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.member')),
            ],
        ),
        migrations.CreateModel(
            name='MemberBio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', tinymce.models.HTMLField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.member')),
            ],
        ),
        migrations.CreateModel(
            name='MemberBankDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BankName', models.CharField(choices=[('ABP', 'Al Baraka Bank (Pakistan) Limited'), ('ABL', 'Allied Bank Limited'), ('AB', 'Askari Bank'), ('BAP', 'Bank Alfalah Limited'), ('BAH', 'Bank Al-Habib Limited'), ('BIP', 'BankIslami Pakistan Limited'), ('BOP', 'Bank of Punjab'), ('FBL', 'Faysal Bank Limited'), ('HBL', 'Habib Bank Limited'), ('JS', 'JS Bank Limited'), ('MCB', 'MCB Bank Limited'), ('MBL', 'Meezan Bank Limited'), ('NBP', 'National Bank of Pakistan'), ('SB', 'Summit Bank Pakistan'), ('UBL', 'United Bank Limited (UBL)')], max_length=255)),
                ('AccountNO', models.IntegerField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.member')),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.team'),
        ),
        migrations.AddField(
            model_name='member',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
