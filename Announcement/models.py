from django.db import models
from datetime import datetime
from django.utils.text import slugify
from tinymce.models import HTMLField

# Create your models here.

class Announcement(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(null=True, blank=True)
    content = HTMLField()
    created_at = models.DateTimeField( default=datetime.now, blank=True)

    def __str__ (self):
        return self.title

    def save(self, *args, **kwargs):
        # if self.slug is None:
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

        # self.slug = slugify(self.Full_name)
        # self.save()