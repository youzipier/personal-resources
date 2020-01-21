from django.shortcuts import render

# Create your views here.
def daydetail(request):
    return render(request, 'daylife/day_detail.html')

def daylist(request):
    return render(request,'daylife/daylist.html')