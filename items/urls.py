from django.urls import path
from . import views
app_name = "items"
urlpatterns = [
    path('new/', views.new_item,name='new'),
    path('<int:pk>/', views.item_detail, name='item_detail'),
    path('delete/<int:pk>/', views.delete_item, name='delete_item'),
]