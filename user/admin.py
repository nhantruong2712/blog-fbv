from django.contrib import admin
from user.models import Profile

# Register your models here.


@admin.register(Profile)
class PersonAdmin(admin.ModelAdmin):
	# list_display = Profile._meta.get_all_field_names() # use for django < 1.9
	list_display = [field.name for field in Profile._meta.get_fields()]  # use for django >=1.9
	list_display_links = ['user']
