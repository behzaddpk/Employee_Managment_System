from django.db import models
from tinymce.models import HTMLField
from AdminModule.models import *
# Create your models here.

class LeaveApplication(models.Model):
    Application_Status = (
        ("Pending", "Pending"),
        ("Approved","Approved"),
        ("Rejected","Rejected")
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField()
    subject = models.CharField(max_length=250)
    application = HTMLField()
    status = models.CharField(choices=Application_Status, max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
    