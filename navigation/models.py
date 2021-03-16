from urllib.parse import urljoin

from django.db import models

# Create your models here.

class BaseMenuItem(models.Model):
	title = models.CharField(max_length=64)
	link = models.CharField(max_length=64)
	base_url = models.CharField(max_length=64, blank=True, null=True)
	login_required = models.BooleanField(default=False)
	anonymous_only = models.BooleanField(default=False)
	order = models.PositiveIntegerField(default=10)  # = 0 or > 0
	new_tab = models.BooleanField(default=False)

	class Meta:
		abstract = True

	@property
	def url(self):
		if self.base_url:
			return urljoin(self.base_url, self.link)  # example.com/ + category
		return self.link


class MenuItem(BaseMenuItem):

	def __str__(self):
		return self.title

	@property
	def sub_menu_items(self):
		return self.submenuitems_set.all().order_by('order')
		# submenuitems_set: 1-many fields or m-m fields, replace related_name, see on migrate

	@property
	def num_sub_menu_items(self):
		return len(self.sub_menu_items)

	@property
	def has_sub_menu_items(self):
		return self.num_sub_menu_items > 0

class SubMenuItems(BaseMenuItem):
	menu = models.ForeignKey(MenuItem, on_delete=models.CASCADE)

	def __str__(self):
		return '{0} {1}'.format(self.menu.title, self.title)