from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify 
from tinymce.models import HTMLField




class CustomUser(AbstractUser):
    USER_CHOICES = (
        ('1', 'ADMIN'),
        ('2', 'PARTNER'),
        ('3', 'CORDINATOR'),
        ('4', 'TEAM LEADER'),
        ('5', 'WRITER'),
        ('6', 'MEMBER'),
    )
    Designate = models.CharField(max_length=50, choices=USER_CHOICES, default=1)
    profile_pic = models.ImageField(upload_to='media/profile_pic')
    slug = models.SlugField(null=True, blank=True)

    def get_designate_display(self):
        return dict(CustomUser.USER_CHOICES).get(self.Designate)
   

    def save(self, *args, **kwargs):
        # if self.slug is None:
        self.slug = slugify(self.username)
        super().save(*args, **kwargs)

        # self.slug = slugify(self.Full_name)
        # self.save()

class CustomUserBio(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    bio = HTMLField()


class CustomUserProfile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    contact_no = models.CharField(max_length=11)
    tag = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255)


class CustomUserSkill(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    skill = models.CharField(max_length=255)

class CustomUserExperience(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    ExperiencedField = models.CharField(max_length=255)
    ExperiencedYear = models.DecimalField(max_digits=3, decimal_places=2)

class CustomUserEducation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    StudyIn = models.CharField(max_length=255)
    PassingYear = models.DateField()

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

class CustomUserBankDetail(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    BankName = models.CharField(choices=BANK_CHOICES, max_length=255)
    AccountNO = models.IntegerField()


