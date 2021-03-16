from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page

from blog.models import Post, Category


# Create your views here.

def posts(request, filter_kwargs={}, search=None):
	objects = Post.visible_posts.filter(**filter_kwargs)
	paginator = Paginator(objects, 10)
	try:
		objects = paginator.page(request.GET.get('page'))  # name = page
	except PageNotAnInteger:
		objects = paginator.page(1)
	except EmptyPage:
		objects = paginator.page(paginator.num_pages)
	context = {'posts': objects, 'search': search}
	return render(request, 'blog/blog.html', context)


@cache_page(60*15)
def blog(request):
	return posts(request)


@cache_page(60*15)
def archive(request, year):
	return posts(request, {'created__year': year})


@cache_page(60*15)
def category(request, slug):
	categories = get_object_or_404(Category, slug=slug)
	return posts(request, {'category': categories})


@cache_page(60*15)
def blog_post(request, year, month, slug): # year, month, slug in <int:year>/<int:month>/<slug:slug>
	post = get_object_or_404(Post, slug=slug)
	return render(request, 'blog/post.html', {'post': post})


def search(request):
	query = request.GET.get('search')  # name input = 'search'
	if query:
		return posts(request, {'content__icontains': query}, search=query)  # icontain: Case-insensitive containment test.
	return posts(request, search=query)

def error(request, *args, **kwargs):
	return render(request, 'blog/404.html')