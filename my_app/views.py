from django.shortcuts import render, get_object_or_404

from .models import MenuItem


def main(request):
    context = {
        'title': "Main Page"
    }

    return render(request, "my_app/main.html", context)


def menu_item_view(request, menu_item_pk):
    menu_item = get_object_or_404(MenuItem, pk=menu_item_pk)

    context = {
        'title': f"Menu Item - {menu_item.name}",
        'active_menu_item': menu_item
    }

    return render(request, "my_app/menu_item.html", context)
