from django.db import models
from django.utils.text import slugify 
from team.models import Team
from AdminModule.models import CustomUser
from tinymce.models import HTMLField




# Create your models here.


class TeamLeader(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='teamleader', null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
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

class TeamLeaderProfile(models.Model):
    user = models.ForeignKey(TeamLeader, on_delete=models.CASCADE)
    contact_no = models.CharField(max_length=11)
    tag = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255)

class TeamLeaderPhoto(models.Model):
    user = models.ForeignKey(TeamLeader, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='Leader')

class TeamLeaderBio(models.Model):
    user = models.ForeignKey(TeamLeader, on_delete=models.CASCADE)
    bio = HTMLField()

class TeamLeaderSkill(models.Model):
    user = models.ForeignKey(TeamLeader, on_delete=models.CASCADE)
    skill = models.CharField(max_length=255)

class TeamLeaderExperience(models.Model):
    user = models.ForeignKey(TeamLeader, on_delete=models.CASCADE)
    ExperiencedField = models.CharField(max_length=255)
    ExperiencedYear = models.DecimalField(max_digits=3, decimal_places=2)

class TeamLeaderEducation(models.Model):
    user = models.ForeignKey(TeamLeader, on_delete=models.CASCADE)
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

class TeamLeaderBankDetail(models.Model):
    user = models.ForeignKey(TeamLeader, on_delete=models.CASCADE)
    BankName = models.CharField(choices=BANK_CHOICES, max_length=255)
    AccountNO = models.IntegerField()