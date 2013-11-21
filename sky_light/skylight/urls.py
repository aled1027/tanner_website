from django.conf.urls import patterns, include, url
from django.contrib import admin
from skylight.views import *
admin.autodiscover()

urlpatterns = patterns('',
	    url(r'^admin/', include(admin.site.urls)),

		url(r'^blog/', include('blog.urls')),

		url(r'^accounts/login/$', 'skylight.views.login'),
		url(r'^accounts/auth/$', 'skylight.views.auth_view'),
		url(r'^accounts/logout/$', 'skylight.views.logout'),
		url(r'^accounts/loggedin/$', 'skylight.views.loggedin'),
		url(r'^accounts/invalid/$', 'skylight.views.invalid_login'),
		url(r'^accounts/register/$', 'skylight.views.register_user'),
		url(r'^accounts/register_success/$', 'skylight.views.register_success'),
#	        url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
