from django import template

from blog.models import Post, Category

register = template.Library()

# Register inclusion tag
@register.inclusion_tag('./blog/tags/_blog_recent.html')
def blog_recent():
	return {'recent': Post.objects.order_by('-created')[:5]}


@register.inclusion_tag('./blog/tags/_blog_categories.html')
def blog_categories():
	return {'categories': Category.objects.order_by('title')}


@register.inclusion_tag('./blog/tags/_blog_archive.html')
def blog_archive():
	posts = Post.visible_posts.order_by('created')
	return {'posts': posts}
