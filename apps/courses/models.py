from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors["name"] = "Course name should be more than 5 characters"
        return errors
class DescriptionManager(models.Manager):
    def basic_validator(self, postData):
        desc_errors = {}
        if len(postData['desc']) < 15:
            desc_errors["desc"] = "Discription should be more than 10 characters"
        return desc_errors        
class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=	True)
    objects = CourseManager()

class Description(models.Model):
    desc = models.TextField()
    course = models.OneToOneField(Course,
        on_delete=models.CASCADE,
        primary_key=True)
    created_at = models.DateField(auto_now_add=	True)
    objects = DescriptionManager()