from django.shortcuts import render
from items.models import Item,Catagory
# Create your views here.

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    catagories = Catagory.objects.all()
    
    return render(request,'core/index.html',{
        'catagories' : catagories ,
        'items' : items
    })



