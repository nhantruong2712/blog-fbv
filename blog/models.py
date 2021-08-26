from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.contrib.sitemaps import ping_google
from django.db import models

# Create your models here.
from django.template.defaultfilters import slugify
from django.utils.html import strip_tags
from django.contrib.contenttypes.fields import GenericRelation

from blog.managers import VisiblePostManager, PostManager


class Category(models.Model):
	title = models.CharField(max_length=64)
	slug = models.SlugField(default='')

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super().save(*args, **kwargs)

	def get_absolute_url(self):  # to view on site
		return '/blog/category/{0}'.format(self.slug)


class Post(models.Model):
	title = models.CharField(max_length=100, default='')
	slug = models.SlugField(default='', unique=True, max_length=100, allow_unicode=True)
	visible = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	content = RichTextUploadingField(blank=True, null=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	click = models.PositiveIntegerField(default=0)

	objects = PostManager()
	visible_posts = VisiblePostManager()

	def __str__(self):
		return self.title + ' | ' + str(self.author)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super().save(*args, **kwargs)
		try:
			ping_google()  # "ping" Google when sitemap change
		except Exception:
			# Bare 'except' because we could get a variety
			# of HTTP-related exceptions.
			pass

	def preview(self, length=300):
		try:
			preview = strip_tags(self.content)[:length]
		except:
			preview = ''
		return preview + '...'

	def short_preview(self):
		return self.preview(length=100)
	short_preview.short_description = 'content'

	def get_date(self):
		return self.created
	get_date.short_description = 'date'

	def get_absolute_url(self):
		return '/blog/{0}/{1:02d}/{2}/'.format(
			self.created.year,
			self.created.month,
			self.slug,
		)
