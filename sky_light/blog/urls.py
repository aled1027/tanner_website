from django.conf.urls import *
from blog.views import *

urlpatterns = patterns("",
	(r'^article-list/$', articleListView, {}, "article_list"),
	(r'^article-detail/(?P<pk>\d+)/$', articleDetailView, {}, "article_detail"),
	(r'^comment-detail/(?P<pk>\d+)/$', commentDetailView, {}, ""),
	(r'^article-detail/(?P<pk>\d+)/comment/(?P<comment_pk>\d+)/$', commentDetailView, {}, "comment_detail"),
	(r'^create-comment/(?P<pk>\d+)/$', commentFormView, {}, "comment_form"),
	(r'^create-rebuttal/(?P<pk>\d+)/$', rebuttFormView, {}, "rebutt_form"),
)
