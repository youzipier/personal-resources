from django.urls import path
from flower import views

app_name = 'flower'
urlpatterns = [
    path('',views.index),
    path('flower_detail/',views.flower_detail,name='f_detail'),
    path('flower_list/',views.flower_list,name='f_list'),
    path('flower_add/',views.flower_add,name='f_add'),
    path('list_ajax/',views.list_ajax)
]
