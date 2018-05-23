from django.conf.urls import url
from django.contrib.auth.views import login, logout

from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^$', views.login_redirect, name='login_redirect'),
    url(r'^login/$', views.login_user, name='login'),
    # url(r'^login/$', login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'logout/$', logout, {'template_name': 'accounts/logout.html', 'next_page': '/'}, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/(?P<pk>\d+)/$', views.view_profile, name='view_profile_with_pk'),
    url(r'^profile/edit/', views.edit_profile, name='edit_profile'),
    url(r'^change-password/$', views.change_password, name='change_password'),
]
