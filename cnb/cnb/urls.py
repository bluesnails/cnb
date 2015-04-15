from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^pro/', include('pro.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
]
