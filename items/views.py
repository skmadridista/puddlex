from django.shortcuts import render,get_object_or_404,redirect
from .models import Item
from .forms import NewItemForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def item_detail(request,pk):
    item = Item.objects.get(pk=pk)
    related_items = Item.objects.filter(category=item.category,is_sold = False).exclude(pk=pk)[:3]
    return render(request,'items/item_detail.html',{'item' : item,
                                                    'related_items' : related_items})

login_required    
def new_item(request):
    
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit =False)
            item.created_by = request.user
            item.save()
            
            return redirect('items:item_detail',pk = item.id)
    else:
        form = NewItemForm()    
    
    return render(request,'items/form.html',{
        'form' : form,
        'title': 'New item'
    })
    
login_required
def delete_item(request,pk):
    item = get_object_or_404(Item,pk=pk,created_by = request.user)
    item.delete()
    
    return redirect('dashboard:index')