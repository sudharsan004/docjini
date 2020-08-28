"""docsfinder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from find import views as findViews
from django.views.generic.base import TemplateView
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap


sitemaps = {
    'static': StaticViewSitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',findViews.home,name='home'),
    path('results',findViews.results,name='results'),
    path('how-to-use-docjini',findViews.howto,name='how-to'),
    path('contact',findViews.contact,name='contact'),
    path('terms',findViews.terms,name='terms'),
    path('privacy',findViews.privacy,name='privacy'),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="find/robots.txt", content_type="text/plain"),
    ),
# path(
#         "sitemap.xml",
#         TemplateView.as_view(template_name="find/sitemap.xml", content_type="text/plain"),
#     ),
path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap')

]
