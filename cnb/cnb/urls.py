from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^pro/', include('pro.urls', namespace="pro")),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
	url(r'^accounts/change-password/$', 'django.contrib.auth.views.password_change'), 
	url(r'^accounts/password-reset/$', 'django.contrib.auth.views.password_reset'), 
	url(r'^accounts/password-changed/$', 'django.contrib.auth.views.password_change_done'),
	url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
]
