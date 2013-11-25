from django.conf.urls import *
from blog.views import *

urlpatterns = patterns("",
	url(r'^article-list/$', articleListView, {}, "article_list"),
	url(r'^article-detail/(?P<pk>\d+)/$', articleDetailView, {}, "article_detail"),
	url(r'^comment-detail/(?P<pk>\d+)/$', commentDetailView, {}, ""),
	url(r'^article-detail/(?P<pk>\d+)/comment/(?P<comment_pk>\d+)/$', commentDetailView, {}, "comment_detail"),
	url(r'^create-comment/(?P<pk>\d+)/$', commentFormView, {}, "comment_form"),
	url(r'^create-rebuttal/(?P<pk>\d+)/$', rebuttFormView, {}, "rebutt_form"),
	url(r'^search/$', 'search_articles', name='search_articles'),
)
