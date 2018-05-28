from django.db import models

# Create your models here.

# Publications Page Model
class Publication(models.Model):
    title = models.CharField(null=True,blank=False,max_length=100,default='No Title')
    link = models.URLField(max_length=256,blank=True)
    description = models.CharField(max_length=256,blank=True)
    publish_year = models.SmallIntegerField(null=True,blank=False)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

# About page model
class About(models.Model):
    content = models.CharField(max_length=1000,blank=False)

    def __str__(self):
        return 'About Me'

# Student model
class Student(models.Model):
    profile = models.ImageField(upload_to='student_image',blank=True)
    name = models.CharField(max_length=256,blank=False)

    PHD = 'PhD'
    MTECH = 'M.Tech'
    MSC = 'M.Sc'
    COURSE_TYPES = (
        (PHD, 'PhD'),
        (MTECH, 'M.Tech'),
        (MSC, 'M.Sc'),
    )
    course = models.CharField(blank=False,choices=COURSE_TYPES,max_length=10)
    research_area = models.CharField(max_length=256,blank=False)
    description = models.CharField(max_length=256,blank=True)

    def __str__(self):
        return self.name

# Projects model
class Project(models.Model):
    name = models.CharField(max_length=256,blank=False)
    sponsored = models.CharField(max_length=256,blank=False)
    principal_investigator = models.CharField(max_length=100,blank=False)
    start_year = models.SmallIntegerField(blank=False)
    end_year = models.SmallIntegerField(blank=True)

    def __str__(self):
        return self.name

# Courses model
class Course(models.Model):
    name = models.CharField(max_length=100,blank=False)
    code = models.CharField(max_length=20,blank=False)
    UNDERGRADUATE = 'UG'
    GRADUATE = 'PG'
    COURSE_TYPES = (
        (UNDERGRADUATE, 'Undergraduate'),
        (GRADUATE, 'Post Graduate'),
    )
    course_type = models.CharField(blank=False,choices=COURSE_TYPES,max_length=2)
    start_year = models.SmallIntegerField(blank=False)
    end_year = models.SmallIntegerField(blank=True)
    semester = models.CharField(blank=True,max_length=25)
    active = models.BooleanField(blank=False,default=False)

    def __str__(self):
        return self.name

# Talks Model
class Talk(models.Model):
    title = models.CharField(blank=False,max_length=256)
    event = models.CharField(blank=False,max_length=256)
    place = models.CharField(blank=False,max_length=256)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False)

    def __str__(self):
        return self.title
