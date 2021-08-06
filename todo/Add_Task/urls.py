
from django.urls import path
from . import views
urlpatterns = [
    path('add_task', views.add_task, name='add_task'),
    path('work_done', views.work_done, name='work_done'),
    path('',views.index, name='index')
    
]
