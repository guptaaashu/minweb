from django.contrib.auth import views as auth_views
from django.conf.urls import include, url
from . import views

urlpatterns = [
url(r'^password-reset/$',auth_views.password_reset,name='password_reset'),
url(r'^password-reset/done/$',auth_views.password_reset_done,name='password_reset_done'),
url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',auth_views.password_reset_confirm,name='password_reset_confirm'),
url(r'^password-reset/complete/$',auth_views.password_reset_complete,name='password_reset_complete'),
url(r'^signup/$', views.signup, name='signup'),
url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),
url(r'^login/$', views.user_login, name='first'),
url(r'^logout/$', views.user_logout, name='logout'),
]
