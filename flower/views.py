from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.shortcuts import redirect
from django.core.paginator import Paginator
from flower.models import *


# Create your views here.
def index(request):
    flower_list = Flower.objects.all()
    return render(request, 'flower/index.html', locals())


def flower_detail(request):
    id = request.GET.get('id')
    flower = Flower.objects.get(id=int(id))
    name = flower.name[-2:]
    flower_list=Flower.objects.filter(name__contains=name)
    print(flower_list)
    picture_list = flower.flowewrpic_set.all()
    return render(request, 'flower/flower_detail.html', locals())


def flower_list(request):
    flower_list = Flower.objects.all()
    paginate = Paginator(flower_list, 4)
    range = list(paginate.page_range)
    print(range)
    return render(request,'flower/flower_list.html',locals())


def list_ajax(request):  #使用vue分页 创建接口
    result = {'code': 200, 'data': []}
    page = request.GET.get('page', 1)
    flower_list = Flower.objects.all()
    paginate = Paginator(flower_list, 4)
    result['page_range'] = list(paginate.page_range)
    print(result['page_range'])
    result['page'] = page
    page_data = paginate.page(int(page))
    for p_data in page_data:
        result_dict = {
            'id':p_data.id,
            'name': p_data.name,
            'introduce': p_data.introduce,
            'picture': p_data.picture.name
        }

        result['data'].append(result_dict)

    return JsonResponse(result,safe=False,json_dumps_params={'ensure_ascii':False})


def flower_add(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        fintroduce = request.POST.get('fintroduce')
        fpicture = request.FILES.get('fpicture')
        f = Flower()
        f.name = fname
        f.introduce = fintroduce
        f.picture = fpicture
        f.save()
        return redirect('flower:f_list')
    return render(request, 'flower/flower_add.html')

