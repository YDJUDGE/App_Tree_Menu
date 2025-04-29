from django.urls import path
from .views import index, page

urlpatterns = [
    path('', index, name='index'),
    path('page/<int:menu_item_pk>/', page, name='page')
]
