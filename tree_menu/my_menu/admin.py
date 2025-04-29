from django.contrib import admin
from .models import Menu, MenuItem

class MenuItemInline(admin.StackedInline):
    model = MenuItem
    extra = 1
    fk_name = 'parent'

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'menu', 'parent')
    list_filter = ('menu',)
    search_fields = ('title',)
    raw_id_fields = ('menu', 'parent')

admin.site.register(Menu)
admin.site.register(MenuItem, MenuItemAdmin)
