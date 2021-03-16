from django import template

from navigation.models import MenuItem

register = template.Library()


@register.inclusion_tag('navigation/tags/navigation.html', takes_context=True)
def build_navigation(context):
	request = context['request']  # context = {'request': request} - get request
	items = MenuItem.objects.all()

	if request.user.is_authenticated:
		items = items.filter(anonymous_only=False)
	else:
		items = items.filter(login_required=False)
	items = items.order_by('order')
	return {'menu_items': items}