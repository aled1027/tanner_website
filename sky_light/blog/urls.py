from django.conf.urls import *
from blog.views import *

urlpatterns = patterns("",
	(r'^article-list/$', ArticleListView, {}, "article_list"),
	(r'^article-detail/(?P<pk>\d+)/$', articleDetailView, {}, "article_detail"),
	(r'^comment-detail/(?P<pk>\d+)/$', commentDetailView, {}, ""),
	#(r'^article-detail/(?P<pk>\d+)/$', ArticleDetailView.as_view(), {}, "article_detail"),
	(r'^article-detail/(?P<pk>\d+)/comment/(?P<comment_pk>\d+)/$', CommentDetailView.as_view(), {}, "comment_detail"),
	(r'^create-comment/(?P<pk>\d+)/$', CommentFormView.as_view(), {}, "comment_form"),
	(r'^create-rebuttal/(?P<pk>\d+)/$', RebuttFormView.as_view(), {}, "rebutt_form"),
)
