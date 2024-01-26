from .models import MenuItem


def menu(request):
    top_menu_items = MenuItem.objects.filter(parent_item=None)
    return {"menu_items": top_menu_items}
