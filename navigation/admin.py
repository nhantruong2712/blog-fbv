from django.contrib import admin
from navigation.models import SubMenuItems, MenuItem

# Register your models here.


class SubMenuItemInline(admin.TabularInline):
	model = SubMenuItems
	ordering = ['order']


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
	list_display = ['order', 'title', 'link', 'num_sub_menu_items',
					'login_required', 'anonymous_only']
	list_display_links = ['title', 'link']
	list_filter = ['login_required', 'anonymous_only']
	list_per_page = 25
	ordering = ['order']
	inlines = [SubMenuItemInline]
