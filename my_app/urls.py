from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('menu_item/<int:menu_item_pk>', views.menu_item_view, name="menu_item"),
]
