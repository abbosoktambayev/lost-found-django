from django.urls import path
from .views import home, item_detail, add_item
from . import api_views

urlpatterns = [
    path('', home, name='home'),
    path('item/<int:item_id>/', item_detail, name='item_detail'),
    path('add/', add_item, name='add_item'),
]

urlpatterns += [
    path('api/items/', api_views.items_api),
    path('api/items/<int:item_id>/', api_views.item_detail_api),
]