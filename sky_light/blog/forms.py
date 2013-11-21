from django.db import models
from django.forms import ModelForm
from blog.models import *

class ArticleForm(ModelForm):
	class Meta:
		model = Article
		exclude = ['']

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		exclude = ['author','article']
	def clean_author(self):
		return self.cleaned_data.get("author") or "Anonymous"

class RebuttForm(ModelForm):
	class Meta:
		model = Rebutt
		exclude = ['author','comment']
