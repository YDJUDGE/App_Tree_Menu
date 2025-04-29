from django.shortcuts import render, get_object_or_404
from .models import MenuItem

def index(request):
    return render(request, 'my_menu/index.html', {})

def page(request, menu_item_pk):
    menu_item = get_object_or_404(MenuItem, pk=menu_item_pk)
    return render(request, 'my_menu/page.html', {'menu_item': menu_item})