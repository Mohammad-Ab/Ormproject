from django.contrib import admin
from .models import Student,Lesson,Package,Course
# Register your models here.

admin.site.register(Student)
admin.site.register(Lesson)
admin.site.register(Package)
admin.site.register(Course)
