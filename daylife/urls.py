from django.urls import path,re_path
from daylife import views

app_name = 'daylife'
urlpatterns = [
    path('daylist/',views.daylist,name='daylist'),
    path('daydetail/',views.daydetail,name='daydetail'),
]