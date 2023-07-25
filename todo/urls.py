from django.urls import path
from .views import index, remove

urlpatterns = [
    path('', index, name='todo'), 
    path('del/<str:item_id>', remove, name='del'), 
]