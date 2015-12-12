from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),


    url(r'^$', 'apps.biblioteca.views.home', name='home'),

    url(r'^biblioteca/$', 'apps.biblioteca.views.biblioteca', name='biblioteca'),
    # url(r'^biblioteca/$', 'apps.biblioteca.views.biblioteca', name='biblioteca'),
    
    url(r'^biblioteca/carrera/(\d+)/$', 'apps.biblioteca.views.biblioteca_carrera', name='biblioteca_carrera'),
    # url(r'^carrera/(?P<carrera>[\w\-]+)', 'apps.biblioteca.views.biblioteca_carrera', name='biblioteca_carrera'),

    url(r'^biblioteca/book/(\d+)/(\d+)/$', 'apps.biblioteca.views.book_detail_view', name='book_detail_view'),
    # url(r'^biblioteca/(?P<title>[\w\-]+)', 'apps.biblioteca.views.book_detail_view', name='book_detail_view'),

    url(r'^hemeroteca/$', 'apps.biblioteca.views.hemeroteca', name='hemeroteca'),

    url(r'^logout/', 'apps.biblioteca.views.LogOut', name='logout'),
    
    url(r'^reserva/(\d+)/(\d+)/$', 'apps.biblioteca.views.reserva', name='reserva'),
]


from django.conf import settings
if settings.DEBUG:
	urlpatterns += patterns("",
		url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
			{'document_root': settings.MEDIA_ROOT,}
		),
	)