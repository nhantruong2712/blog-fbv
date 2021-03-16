from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from blog.models import Post, Category


class BlogPostSiteMap(Sitemap):
	changefreq = "yearly"  # change frequency
	priority = 0.5  # 0 - 1.0. Default is 0.5

	def items(self):
		return Post.objects.all()

	def lastmod(self, obj):  # last modify
		return obj.created


class BlogCategorySiteMap(Sitemap):
	changefreq = "yearly"
	priority = 0.5

	def items(self):
		return Category.objects.all()

# class StaticViewSitemap(Sitemap):
# 	changefreq = 'yearly'
# 	priority = 0.5
#
# 	def items(self):
# 		return 'blog:blog_post/{0}/{1:02d}/{2}/'.format(
# 			self.created.year,  # has no attribute created, fix later
# 			self.created.month,
# 			self.slug,
# 		)
#
# 	def location(self, item):
# 		return reverse(item)
