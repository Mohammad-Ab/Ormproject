from django.shortcuts import render
from .models import Student
# Create your views here.
def Index(request):
    queryset = Student.objects.all()
    print(queryset)
    return render(request,'student/index.html',{'students':queryset})

