from django.db import models
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.text import slugify
from AdminModule.models import CustomUser
# Create your models here.



class Client(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    Full_name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, null=True)
    email = models.EmailField(max_length=50)
    country = models.CharField(max_length=50)
    contactno = models.IntegerField(blank=True)
    bank_account = models.CharField(max_length=70, blank=True)
    weblink = models.URLField(max_length=50, blank=True)
    img = models.FileField(upload_to='client')

    def save(self, *args, **kwargs):
        # if self.slug is None:
        self.slug = slugify(self.Full_name)
        super().save(*args, **kwargs)

        # self.slug = slugify(self.Full_name)
        # self.save()
    
    def __str__(self):
        return self.Full_name
    

def slugify_name(instance, save=False):
    slug = slugify(instance.Full_name)
    qs = Client.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        slug = f"{slug} -{qs.count} + 1"
    instance.slug = slug 
    if save:
        instance.save()
    return instance


def Client_pre_save(sender, instance, *args, **kwargs):
    print('pre_sav')
    print(sender, instance)
    if instance.slug is None:
        slugify_name(instance, save=False)

pre_save.connect(Client_pre_save, sender=Client)

    
def Client_post_save(sender, instance, created, *args, **kwargs):
    print('post_save')
    if created:
        slugify_name(instance, save=True)
post_save.connect(Client_post_save, sender=Client)
