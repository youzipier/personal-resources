from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'animal/animal_index.html')

def list(request):
    return render(request,'animal/animal_list.html')

def add(request):
    return render(request,'animal/animal_add.html')
