from django.shortcuts import render
from .models import Student,Package,Lesson,Course,Teacher
from django.db.models import Q
# Create your views here.
def Index(request):
    #queryset = Student.objects.all()
    #queryset = Student.objects.filter(course__lesson__name="Math")
    #queryset = Package.objects.filter(course__lesson__name="Physic", course__students__name="Gisoo")
    #queryset = Package.objects.filter(Q(course__lesson__name="Physic") & Q(course__students__name="Gisoo"))
    #queryset = Package.objects.filter(course__students__name).exclude(name__in=['Gisoo','Sima'])
    #queryset = Package.objects.filter(course__lesson__name="Math").values("name","course__name","course__description")
    #queryset = Package.objects.filter(course__lesson__name="Math").values_list("name","course__name","course__description")
    #queryset = Package.objects.filter(course__students__name="Gisoo").distinct() /* dont repeat Packages name*/
    
    #queryset = Package.objects.all().order_by('course__students__name','course__name').values('name','course__students__name','course__lesson__name')
    qs1=Student.objects.all().values_list("name","nationalcode")
    qs2=Teacher.objects.all().values_list("fullname","nationalcode")

    queryset = qs1.union(qs2)

    print(queryset)
    return render(request,'student/index.html',{'students':queryset})

