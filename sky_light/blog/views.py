from django.shortcuts import get_object_or_404
from django.core.context_processors import csrf
import time
from calendar import month_name
from blog.models import *
from blog.forms import *
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, UpdateView, CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import Http404
from getArticle import *

def homeView(request):
	args = {}
	return render(request, "home.html", args)

def articleListView(request):
	addArticlesFromGoose(5)
	args = {}
	args.update(csrf(request))
	arts = []

    # probably remove the all -- only get 21 articles or so.
	arts = list(Article.objects.all())
	args['articles1'] = []
	args['articles2'] = []
	args['articles3'] = []
	for x in range(0, len(arts)):
		if (x%3) == 0:
			args['articles1'].append(arts[x])
		if (x%3) == 1:
			args['articles2'].append(arts[x])
		if (x%3) == 2:
			args['articles3'].append(arts[x])


	return render(request, "list.html", args)

def articleDetailView(request, pk):  #successful!
	try:
		a = Article.objects.get(pk=pk)
	except Article.DoesNotExist:
		raise Http404
	return render(request, "detail.html", {"article": a})

def articleCreateView(request, a_id=None):
	if a_id:
		a = Article.objects.get(pk=a_id)
	else:
		a = None
	if request.method == 'POST':
		form = ArticleForm(request.POST, request.FILES)
		if form.is_valid():
			form.save
			return HttpResponseRedirect(reverse('article-detail', args=[form.article.id]))
   	else:
		form = MembershipForm(instance=a)
		return render(request, 'article_form.html', {'form': form})

#not sure if this works
def commentDetailView(request, pk):
	try:
		c = Comment.objects.get(pk=pk)
	except Comment.DoesNotExist:
		raise Http404
	f = RebuttForm() #can also do f = rebuttform(instance = s)
	# also check out form sets for multiple forms on a page
	return render(request, "comment_detail.html", {'comment': c, 'form': f})

def commentFormView(request, a_id = None, c_id=None):
	if c_id:
		c = Comment.objects.get(pk=c_id)
	else:
		c = None
	if request.method == 'POST':
		form = CommentForm(request.POST, request.FILES)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.article = get_object_or_404(Article, pk=a_id)
			comment.save()
			return HttpResponseRedirect(reverse('article_detail', args=[a_id]))
	else:
		form = CommentForm(instance=c)
		return render(request, 'comment_form.html', {'form': form})

def rebuttFormView(request, r_id=None):
	if r_id:
		r = Comment.objects.get(pk=r_id)
	else:
		r = None
	if request.method == 'POST':
		form = CommentForm(request.POST, request.FILES)
		if form.is_valid():
			form.save
			return HttpResponseRedirect(reverse('comment-detail', args=[form.comment.id]))
	else:
		form = MembershipForm(instance=r)
		return render(request, 'article_form.html', {'form': form})

def search_articles(request):
	if request.method == 'POST':
		search_text = request.POST['search_text']
	else:
		search_text = ''
	articles = Article.objects.filter(title__contains=search_text)
	return render(request, 'ajax_search.html', {'articles': articles})

def searchPageView(request):
	# Need to actually make this.
	return render(request, 'search_page.html', {});



