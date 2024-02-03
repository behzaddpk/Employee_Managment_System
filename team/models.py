from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from tinymce.models import HTMLField
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.contrib.auth.models import AbstractUser
from AdminModule.models import CustomUser
# Create your models here.

class Team(models.Model):
    team_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.team_name

    

class Designation(models.Model):
    designation = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.designation



class Member(models.Model):
    user= models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    is_varified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add= True)


    
        # self.save()
    def __str__(self):
        return self.user.username



class MemberProfile(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    contact_no = models.CharField(max_length=11)
    tag = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255)

class MemberPhoto(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='Partner')

class MemberBio(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    bio = HTMLField()

class MemberSkill(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    skill = models.CharField(max_length=255)

class MemberExperience(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    ExperiencedField = models.CharField(max_length=255)
    ExperiencedYear = models.DecimalField(max_digits=3, decimal_places=2)


BANK_CHOICES = (
    ('ABP','Al Baraka Bank (Pakistan) Limited'),
    ('ABL','Allied Bank Limited'),
    ('AB','Askari Bank'),
    ('BAP','Bank Alfalah Limited'),
    ('BAH','Bank Al-Habib Limited'),
    ('BIP','BankIslami Pakistan Limited'),
    ('BOP','Bank of Punjab'),
    ('FBL','Faysal Bank Limited'),
    ('HBL','Habib Bank Limited'),
    ('JS','JS Bank Limited'),
    ('MCB','MCB Bank Limited'),
    ('MBL','Meezan Bank Limited'),
    ('NBP','National Bank of Pakistan'),
    ('SB','Summit Bank Pakistan'),
    ('UBL','United Bank Limited (UBL)'),
)

class MemberBankDetail(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    BankName = models.CharField(choices=BANK_CHOICES, max_length=255)
    AccountNO = models.IntegerField()


class MemberEducation(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    StudyIn = models.CharField(max_length=255)
    PassingYear = models.DateField()


class MemberEvaluation(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    Monthevaluate = models.DateField()
    Punctuality = models.FloatField(max_length=1,validators=[MinValueValidator(1), MaxValueValidator(5)])
    Attitude = models.FloatField(max_length=1,validators=[MinValueValidator(1), MaxValueValidator(5)])
    Performance = models.FloatField(max_length=1,validators=[MinValueValidator(1), MaxValueValidator(5)])
    Utilities = models.FloatField(max_length=1,validators=[MinValueValidator(1), MaxValueValidator(5)])
    Formatiing = models.FloatField(max_length=1,validators=[MinValueValidator(1), MaxValueValidator(5)])
    Quality = models.FloatField(max_length=1,validators=[MinValueValidator(1), MaxValueValidator(5)])
    Expertise = models.FloatField(max_length=1,validators=[MinValueValidator(1), MaxValueValidator(5)])
    New_Learning = models.FloatField(max_length=1,validators=[MinValueValidator(1), MaxValueValidator(5)])
    Planning = models.FloatField(max_length=1,validators=[MinValueValidator(1), MaxValueValidator(5)])
    AI_Flowed = models.FloatField(max_length=1,validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return str(self.member)

    @property
    def allsum(self):
        return self.Punctuality + self.Attitude + self.Performance + self.Utilities + self.Formatiing + self.Quality + self.Expertise + self.New_Learning + self.Planning + self.AI_Flowed