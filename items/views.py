from django.shortcuts import render,get_object_or_404
from .models import Item,Category
# Create your views here.
def item_detail(request,pk):
    item = Item.objects.get(pk=pk)
    related_items = Item.objects.filter(category=item.category,is_sold = False).exclude(pk=pk)[:3]
    return render(request,'items/item_detail.html',{'item' : item,
                                                    'related_items' : related_items})