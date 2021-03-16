from django.urls import path
from blog import views
from blog.feeds import BlogFeed, BlogAtomFeed

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='blog'),
    path('archive/<int:year>', views.archive, name='blog_archive'),
    path('category/<slug:slug>', views.category, name='blog_category'),
    path('<int:year>/<int:month>/<slug:slug>', views.blog_post, name='blog_post'),
    path('search/', views.search, name='blog_search'),
    path('feed/rss/', BlogFeed(), name='blog_rss'),
    path('feed/atom/', BlogAtomFeed(), name='blog_atom'),
]



