from django.shortcuts import render
from .models import Student,Package,Lesson,Course
from django.db.models import Q
# Create your views here.
def Index(request):
    #queryset = Student.objects.all()
    #queryset = Student.objects.filter(course__lesson__name="Math")
    #queryset = Package.objects.filter(course__lesson__name="Physic", course__students__name="Gisoo")
    queryset = Package.objects.filter(Q(course__lesson__name="Physic") & Q(course__students__name="Gisoo"))
    print(queryset)
    return render(request,'student/index.html',{'students':queryset})

