# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from django.db import models

class Education(models.Model):

    fromYear = models.IntegerField()
    toYear = models.IntegerField()
    nameOfDegree = models.CharField(max_length=100)
    nameOfInstitution = models.CharField(max_length=500)
    desc = models.CharField(max_length=200)

    # img = models.ImageField(upload_to='pics')
    # price = models.IntegerField()
    # offer = models.BooleanField(default=False)

class Experience(models.Model):

    fromYear = models.IntegerField()
    toYear = models.IntegerField()
    nameOfPost = models.CharField(max_length=100)
    nameOfCompany = models.CharField(max_length=500)
    desc = models.CharField(max_length=200)


class Awards(models.Model):

    when = models.IntegerField()
    nameOfAwards = models.CharField(max_length=100)
    awardFrom = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)

class Projects(models.Model):

    projectTitle = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    projectType = models.CharField(max_length=200)

class Blog(models.Model):

    blogTitle = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.CharField(max_length=2000)
