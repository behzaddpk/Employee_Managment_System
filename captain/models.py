from django.db import models
from clients.models import Client
from team.models import Member
from django.utils.text import slugify
# from django.contril.auth.model import User

# Create your models here.

class TaskCategory(models.Model):
    taskname = models.CharField(max_length=50, unique=True)


    def __str__(self):
        return self.taskname


class InstitutionName(models.Model):
    InstitutionName = models.CharField(max_length=50, unique=True)


    def __str__(self):
        return self.InstitutionName


class AssessmentType(models.Model):
    AssessmentName = models.CharField(max_length=50, unique=True)


    def __str__(self):
        return self.AssessmentName

STATUS_CHOICE = (
    ('Pending', 'Pending'),
    ('Do Able', 'Do Able'),
    ('Accepted', 'Accepted'),
    ('Cancel', 'Cancel'),
    ('Working', 'Working'),
    ('Delivered','Delivered'),
)

class TaskDetail(models.Model):
    task_name = models.CharField(max_length=50)
    slug = models.SlugField(default=True, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    task_category = models.ForeignKey(TaskCategory, on_delete=models.CASCADE)
    institution_name = models.ForeignKey(InstitutionName, on_delete=models.CASCADE)
    deadline = models.DateField(null=True, blank=True)
    course_code = models.CharField(max_length=10)
    # course_name = models.CharField(max_length=50)
    instruction = models.CharField(max_length=126)
    word_count = models.IntegerField()
    assessment_type = models.ForeignKey(AssessmentType, on_delete=models.CASCADE)
    attachment_file = models.FileField(upload_to='task')
    send_to = models.ForeignKey(Member, on_delete=models.CASCADE, default=True, null=False)
    task_status = models.CharField(choices=STATUS_CHOICE, max_length=25, null=True, default='Pending')

    def save(self, *args, **kwargs):
        # if self.slug is None:
        self.slug = slugify(self.task_name)
        super().save(*args, **kwargs)

        # self.slug = slugify(self.Full_name)
        # self.save()


    def __str__(self):
        return self.task_name