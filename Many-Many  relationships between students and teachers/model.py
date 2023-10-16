from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    teachers = models.ManyToManyField('Teacher', related_name='students')

class Teacher(models.Model):
    name = models.CharField(max_length=100)
