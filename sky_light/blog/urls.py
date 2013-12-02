from django.conf.urls import *
from blog.views import *

urlpatterns = patterns("",
	url(r'^article-list/$', articleListView, {}, "article_list"),
	url(r'^article-detail/(?P<pk>\d+)/$', articleDetailView, {}, "article_detail"),
	url(r'^comment-detail/(?P<pk>\d+)/$', commentDetailView, {}, "comment_detail"),
	#url(r'^article-detail/(?P<pk>\d+)/comment/(?P<comment_pk>\d+)/$', commentDetailView, {}, "comment_detail"),
			#not sure what this is doing.. looks like it needs fixin
	url(r'^create-comment/(?P<pk>\d+)/$', commentFormView, {}, "comment_form"),
	url(r'^create-rebuttal/(?P<pk>\d+)/$', rebuttFormView, {}, "rebutt_form"),
	url(r'^search/$', search_articles, {}, "search_articles"),
	url(r'^search/$', searchPageView, {}, "search_page"),
)
