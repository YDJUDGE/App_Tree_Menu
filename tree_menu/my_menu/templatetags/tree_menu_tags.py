from django import template
from my_menu.models import Menu, MenuItem

register = template.Library()

@register.inclusion_tag('my_menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_path = request.path

    try:
        menu_items = list(MenuItem.objects.filter(menu__name=menu_name).select_related('parent'))
    except MenuItem.DoesNotExist:
        return {'menu_items': [], 'active_ids': []}

    if not menu_items:
        return {'menu_items': [], 'active_ids': []}

    # Строим словарь для быстрого доступа
    menu_dict = {item.pk: item for item in menu_items}

    # Строим дерево
    tree = []
    for item in menu_items:
        item.child_list = []
    for item in menu_items:
        if item.parent_id:
            if item.parent_id in menu_dict:
                menu_dict[item.parent_id].child_list.append(item)
        else:
            tree.append(item)

    # Находим активный пункт
    active_item = None
    for item in menu_items:
        if item.get_absolute_url() == current_path:
            active_item = item
            break

    # Собираем active_ids
    active_ids = set()
    if active_item:
        parent = active_item
        while parent:
            active_ids.add(parent.pk)
            parent = parent.parent
        active_ids.update(child.pk for child in active_item.child_list)
    else:
        for item in tree:
            active_ids.add(item.pk)

    return {
        'menu_items': tree,
        'active_ids': active_ids,
    }