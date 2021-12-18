from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
class Career(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.company
    
class Education(models.Model):
    school = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    end_date = models.DateField()
    description = models.TextField()
    
    def __str__(self) -> str:
        return self.school
    
class Project(models.Model):
    project_title = models.CharField(max_length=200)
    project_link = models.URLField(max_length=200)
    image = models.ImageField(upload_to = 'project_image/')
    image_2x = models.ImageField(upload_to = 'project_image2x/')
    header_image = models.ImageField(upload_to = 'header/')
    description = models.TextField()
    tag = TaggableManager()
    
    def __str__(self) -> str:
        return self.project_title
    
class Testimonial(models.Model):
    image = models.ImageField(upload_to = 'testimonial/')
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    testimony = models.TextField()
    
    def __str__(self) -> str:
        return self.name
    
class Social(models.Model):
    name = models.CharField(max_length=100)
    address = models.URLField(max_length=100)
    
    def __str__(self) -> str:
        return self.name