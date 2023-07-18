from django.db import models

# Create your models here.
class Teacher(models.Model):
    fullname = models.CharField(max_length=100)
    nationalcode = models.CharField(max_length=10,null=True)

class Student(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="This is a Student.")
    nationalcode = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="This is a Lesson.")

    def __str__(self):
        return self.name

class Package(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="This is a Package.")

    def __str__(self):
        return self.name

class Course(models.Model):
    package = models.ForeignKey(Package,on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    name = models.CharField(max_length=100)
    description = models.TextField(default="This is a Course")

    def __str__(self):
        return self.name
