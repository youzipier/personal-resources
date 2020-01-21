from django.urls import path,re_path
from animal import views

app_name = 'animal'
urlpatterns = [
    path('index/',views.index,name='a_index'),
    path('list/',views.list,name = 'a_list'),
    path('add/',views.add,name = 'a_add'),

]