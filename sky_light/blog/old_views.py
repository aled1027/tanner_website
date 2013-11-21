from django.shortcuts import get_object_or_404
import time
from calendar import month_name
from blog.models import *
from blog.forms import *
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, UpdateView, CreateView
from django.views.generic.detail import DetailView

class ArticleListView(ListView):
	model = Article 
	template_name="list.html"

	def get_context_data(self, **kwargs):
		context = super(ArticleListView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		return context

class ArticleCreateView(FormView):
	form_class = ArticleForm
	template_name = "article_form.html"
	#add success template
	
	def form_valid(self, form):
		if form.is_valid:
			post = form.save() #why is this 'post' here?
			return super(ArticleCreateView, self).form_valid(form)

class ArticleDetailView(DetailView):
	model = Article
	template_name = "detail.html"

	def get_context_data(self, **kwargs):
		context = super(ArticleDetailView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		context['form'] = CommentForm 
		return context

class CommentFormView(FormView):
	form_class = CommentForm
	success_url = "/blog/post-list"  #fix this
	template_name="post_form.html"
	
	def form_valid(self, form):
		if form.is_valid:
			#kwargs = super(CommentFormView, self).get_form_kwargs()
			#print kwargs
			comment = form.save()	
			return super(CommentFormView, self).form_valid(form)


#class Main(ListView):
#	model = Post
#	paginate_by = 10
#	template_name = "list.html"
#
#	def months(self):
#		if not Post.obj.count(): return list()
#	
#		current_year, current_month = time.localtime()[:2]
#		first = Post.obj.oder_by("created")[0]
#		first_year = first.created.year
#		first_month = first.created.month
#		months = list()
#
#		for year in range(current_year, first_year-1, -1):
#			start, end = 12, 0
#			if year == current_year : start = current_month
#			if year == first_year : end = first_month - 1
#
#			for month in range(start, end, -1):
#				if Post.obj.filter(created_year=year, created_month=month):
#					months.append((year, month, month_name[month]))
#
#		return months


#class ArchiveMonth(Main):
#	paginate_by = None
#	
#	def get_list_queryset(self):
#		year, month = self.args
#		return Post.obj.filter(created_year=year, created_month=month).order_by("created")
