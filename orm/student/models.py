from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="This is a Student.")

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
