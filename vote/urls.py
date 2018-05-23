from django.conf.urls import url, include
from . import views


app_name = 'vote'
urlpatterns = [
    url(r'^upvote/$', views.upvote, name='upvote'),
    url(r'^upvote/(?P<blog_pk>\d+)/$', views.upvote, name='upvote_pk'),
    url(r'^favorite/(?P<fave>.+)/(?P<blog_pk>\d+)$', views.favorite, name='favorite'),
    url(r'^my-favorites/$', views.show_favorites, name='show_favorites'),
    url(r'^add-tag/(?P<blog_pk>\d+)/$', views.add_tag, name='add_tag'),
    url(r'^change-tag/(?P<blog_pk>\d+)?/(?P<tag_name>.+)/(?P<action>.+)$', views.change_tag, name='change_tag'),
    url(r'^change-tag/(?P<blog_pk>\d+)?/(?P<action>.+)$', views.change_tag, name='change_tag'), # add tag
]
