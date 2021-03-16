from django.contrib import admin
from django.urls import path, include
from django.contrib.flatpages import views
from django.contrib.flatpages.sitemaps import FlatPageSitemap
from django.contrib.sitemaps.views import sitemap
from django.conf.urls import handler404

from blog.sitemaps import BlogPostSiteMap, BlogCategorySiteMap  # , StaticViewSitemap
from blog.views import blog
from blogfbv import settings

sitemaps = {
    'page': FlatPageSitemap,
    'blog_post': BlogPostSiteMap,
    'blog_category': BlogCategorySiteMap,
    # 'static': StaticViewSitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', blog),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('<url>/', views.flatpage),
]

handler404 = 'blog.views.error'

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
