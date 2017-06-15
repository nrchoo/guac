from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^create_account/$', views.create_account, name ='create_account'),
    url(r'^logout$',views.logout_view, name='logout_view'),
    url(r'^login/$', views.login_view, name='login_view'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^shopping/$', views.shopping, name='shopping'),
    url(r'^checkout/$', views.checkout, name='checkout'),


]
