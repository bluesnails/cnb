from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^add_ques/', views.add_ques, name='add_ques'),
]
