from django.shortcuts import render
from .models import Menu

# Create your views here.

def menu_list(request):
    menu_list = Menu.objects.all()
    context = {'menu_list': menu_list,}

    return render(request, 'Menu/list.html', context)

def menu_detail(request, slug):
    pass