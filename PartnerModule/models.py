from django.db import models
from django.utils.text import slugify 
from team.models import Team
from django.contrib.auth.models import User
from AdminModule.models import CustomUser
from tinymce.models import HTMLField




# Create your models here.


class Partner(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='partner', null=True)
    team_captain = models.ForeignKey(Team, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)



    def __str__ (self):
        return self.user.username

    def save(self, *args, **kwargs):
        # if self.slug is None:
        self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)

        # self.slug = slugify(self.Full_name)
        # self.save()

class PartnerProfile(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    contact_no = models.CharField(max_length=11)
    tag = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255)

class PartnerPhoto(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='Partner')

class PartnerBio(models.Model):
    Partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    bio = HTMLField()

class PartnerSkill(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    skill = models.CharField(max_length=255)

class PartnerExperience(models.Model):
    Partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    ExperiencedField = models.CharField(max_length=255)
    ExperiencedYear = models.DecimalField(max_digits=3, decimal_places=2)

class PartnerEducation(models.Model):
    Partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
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

class BankDetail(models.Model):
    Partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    BankName = models.CharField(choices=BANK_CHOICES, max_length=255)
    AccountNO = models.IntegerField()