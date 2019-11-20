from django.urls import path, include
from app1 import views as app_views

urlpatterns = [
path('',app_views.show, name='show'),
path('update/',app_views.update, name='update'),
path('add/',app_views.add,name='add'),
path('delete/',app_views.delete,name='delete')
]