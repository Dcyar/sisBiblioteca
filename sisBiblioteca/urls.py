"""sisBiblioteca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),


    url(r'^$', 'apps.biblioteca.views.home', name='home'),

    url(r'^biblioteca/$', 'apps.biblioteca.views.biblioteca', name='biblioteca'),
    # url(r'^biblioteca/$', 'apps.biblioteca.views.biblioteca', name='biblioteca'),
    
    url(r'^biblioteca/carrera/(\d+)/$', 'apps.biblioteca.views.biblioteca_carrera', name='biblioteca_carrera'),
    # url(r'^carrera/(?P<carrera>[\w\-]+)', 'apps.biblioteca.views.biblioteca_carrera', name='biblioteca_carrera'),

    url(r'^biblioteca/book/(\d+)/$', 'apps.biblioteca.views.book_detail_view', name='book_detail_view'),
    # url(r'^biblioteca/(?P<title>[\w\-]+)', 'apps.biblioteca.views.book_detail_view', name='book_detail_view'),

    url(r'^hemeroteca/$', 'apps.biblioteca.views.hemeroteca', name='hemeroteca'),

    url(r'^logout/', 'apps.biblioteca.views.LogOut', name='logout'),
]


from django.conf import settings
if settings.DEBUG:
	urlpatterns += patterns("",
		url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
			{'document_root': settings.MEDIA_ROOT,}
		),
	)