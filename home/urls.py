# Author: Zaid Al-Momen
# 95-882 Enterprise Web Development - Spring 2018. Carnegie Mellon University
#
# SOURCES AND REFERENCES:
#
# Django Tutorials
# https://www.youtube.com/watch?v=Fc2O3_2kax8&list=PLw02n0FEB3E3VSHjyYMcFadtQORvl1Ssj
#
# WYSIWYG - summernote
# https://github.com/summernote/django-summernote
#
# BOOTSRAP CSS and JS
# https://getbootstrap.com/
#
# FAVORITES
# https://simpleisbetterthancomplex.com/tutorial/2016/10/13/how-to-use-generic-relations.html
#
# TAGGING
# https://github.com/alex/django-taggit
##############################################################################

from django.conf.urls import url
from . import views

from home.views import HomeView

app_name = 'home'

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^search/$', views.search, name='search'),
    url(r'^search-nlp/$', views.search_nlp, name='search_nlp'),
    url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_friends, name='change_friends'),
    url(r'^blog/$', views.view_blog, name='view_blog'),
    url(r'^blog/all/$', views.all_blogs, name='all_blogs'),
    url(r'^blog/(?P<pk>\d+)$', views.view_blog, name='view_blog_with_pk'),
    url(r'^blog/edit/(?P<pk>\d+)/$', views.edit_blog, name='edit_blog_with_pk'),
    url(r'^blog/comment/(?P<pk>\d+)/$', views.add_blog_comment, name='add_blog_comment'),
    url(r'^blog/create/$', views.create_blog, name='create_blog'),

]
