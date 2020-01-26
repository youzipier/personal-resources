from django.urls import path,re_path
from daylife import views

app_name = 'daylife'
urlpatterns = [
    path('daylist/',views.daylist,name='daylist'),
    path('daydetail/',views.daydetail,name='daydetail'),
    path('dayregister/',views.register,name='dayregister'),
    path('username_ajax/',views.username_ajax),
    path('daylogin/',views.login,name='daylogin'),
    path('daylife_add/',views.daylife_add,name='daylife_add'),
    path('daylife_delete/',views.daylife_delete,name='daylife_delete'),
    path('daydetail_add/',views.daydetail_add,name='daydetail_add'),
    path('daylife_echart',views.echart,name='dayechart')
]