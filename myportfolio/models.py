from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from pyuploadcare.dj.models import ImageField

# Create your models here.
class Technology(models.Model):
    techlogo = ImageField(manual_crop='200x200')
    technologies = models.CharField(max_length=100)

    def __str__(self):
        return self.technologies

    def save_technology(self):
        self.save()

    @classmethod
    def delete_technology(cls,technologies):
        cls.objects.filter(technologies=technologies).delete()

class Project(models.Model):
    title = models.CharField(max_length=150)
    description = HTMLField()
    # role= models.CharField(max_length=255)
    githublink= models.CharField(max_length=255)
    weblink= models.CharField(max_length=255)
    # logo = models.ImageField(upload_to='projectlogo/')
    screenshot = ImageField(manual_crop='1280x720')
    technologies = models.ManyToManyField(Technology)


    def __str__(self):
        return self.title