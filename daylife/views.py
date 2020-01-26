from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,JsonResponse

from .forms import *
from .models import *

# Create your views here.

def register(request):
    if request.method=='POST':
        data_vaild = UserForm(request.POST)
        if data_vaild.is_valid():
            data = data_vaild.cleaned_data
            email = data.get("email")
            username = data.get("username")
            pwd = data.get("pwd2")
            user = User()
            user.username = username
            user.email = email
            user.password = pwd
            user.save()
            return HttpResponseRedirect('/daylife/daylogin/')
    return render(request,'daylife/register.html')


def username_ajax(request):
    result = {'code':400,'data':''}
    name = request.GET.get('name')
    user = User.objects.filter(username=name).first()
    if user:
        result['data'] ='用户名称已存在'
    else:
        result['data'] = ''
    return JsonResponse(result)


def login(request):
    if request.method =="POST":
        email = request.POST.get("email")
        pwd = request.POST.get('pwd1')
        user = User.objects.filter(email=email).first()
        if user:
            name = user.username
            id = user.id
            if user.password == pwd:
                response = HttpResponseRedirect('daylife:daylist')
                response.set_cookie('name',name)
                response.set_cookie('id',id)
                request.session['id']=id
                return response
    return render(request,'daylife/login.html')

def daydetail(request):
    # 列表页传来的日常id
    id = request.GET.get('id')
    if id:
        # 取日常故事对象显示到详情页
        life = Daylife.objects.filter(id=int(id)).first()
        # 取日常对应的详情故事
        story = life.daystory_set.all().last()
        # 查相关案例的推荐
        d_list = Daylife.objects.all()
    return render(request, 'daylife/day_detail.html',locals())

def daylist(request):
    d_list = Daylife.objects.all()
    return render(request,'daylife/daylist.html',locals())

# 对日常进行添加
def daylife_add(request):

    if request.method =='POST':
        title = request.POST.get('title')
        date = request.POST.get('date')
        detail = request.POST.get('introduce')
        picture = request.FILES.get('picture')
        d = Daylife()
        d.title = title
        d.date = date
        d.detail = detail
        d.logo = picture
        d.save()
        return redirect('daylife:daylist')
    return render(request,'daylife/daylife_add.html')

# 日常删除细节也跟着删除
def daylife_delete(request):
    id = request.GET.get('id') #这个id是点细节传过去的id
    Daylife.objects.get(id=int(id)).delete()
    return redirect('daylife:daylist')

# 对故事的详情进行添加
def daydetail_add(request):
    id = request.GET.get('id') #当前想要查找的详情id
    life = Daylife.objects.filter(id=int(id)).first()
    obj = life.daystory_set.all().first()
    dstory = obj.story
    # 是否有对应故事详情
    story_list = Daylife.objects.all()
    if request.method =='POST':
        pid = request.POST.get('pid') #外键id
        title = request.POST.get('title')
        story = Daylife.objects.get(id=int(pid))
        picture = request.FILES.get('picture')
        if not obj:
            obj = Daystory()
        obj.story = title
        obj.daylife=story
        obj.pic=picture
        obj.save()
        return redirect('/daylife/daydetail/?id='+id)
    return render(request,'daylife/daydetail_add.html',locals())

def echart(request):
    return render(request,'daylife/echart.html')