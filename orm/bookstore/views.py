from django.shortcuts import render
from .models import Book, Store
from django.db.models import Avg,Count,Max,IntegerField
# Create your views here.
def Index(request):
    #books = Book.objects.all().values("name","price","rating").aggregate(books_avg_price=Avg("price"))
    store = Store.objects.filter(name="East").aggregate(books_count=Count("books"), price_max=Max("books__price"), rate_avg=Avg("books__rating",output_field=IntegerField()))
    print(store)
    books = Book.objects.all().annotate(Count("authors")).aggregate(Avg("price"))
    print(books)
    
    return render(request,"bookstore/index.html",{"books":books})
