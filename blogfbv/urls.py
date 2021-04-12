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
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('accounts/', include('user.urls', namespace='accounts')),
    path('todoapp/', include('todoapp.urls', namespace='todoapp')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

handler404 = 'blog.views.error'

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

''' path('accounts/', include('django.contrib.auth.urls')) include:
accounts/login/ [name='login']
accounts/logout/ [name='logout']
accounts/password_change/ [name='password_change']
accounts/password_change/done/ [name='password_change_done']
accounts/password_reset/ [name='password_reset']
accounts/password_reset/done/ [name='password_reset_done']
accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/reset/done/ [name='password_reset_complete'] '''