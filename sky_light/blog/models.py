from django.db.models import *
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.core.mail import send_mail
from taggit.managers import TaggableManager
from goose import Goose
import bs4Mod
import nltk


class Article(models.Model):
	#this needs to be changed ot the current user
	title = CharField(max_length=60, unique=True)
	author = CharField(max_length=60, blank=True)
	source = CharField(max_length=60)
	body = TextField(blank=True)
	bodySummary = TextField(blank=True)
	upvotes = IntegerField(default=0)
	downvotes = IntegerField(default=0)
	added = DateTimeField(auto_now_add=True)
	publish_date = DateTimeField(blank=True)
	url = CharField(max_length=1000, blank=True, unique=True)
	tags = TaggableManager()

	class Meta:
		ordering = ["upvotes"]

	def __unicode__(self):
		return self.title

def addArticlesFromGoose(numArticles = 5):
	# numArticles = number of articles to add
	urls = bs4Mod.getURLS(numArticles)
	artList = []
	g = Goose()
	for url in urls:
		a = g.extract(url=url)
		try:
			obj = Article.objects.get(title=a.title)
			if obj is None:
				raise
		except:
			# check if article/url is valid
			if not (len(a.cleaned_text) > 0):
				return

			# make the body summary a manageable size
			sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
			sList = sent_detector.tokenize(a.cleaned_text.strip())
			bodySummary = ""
			i = 0
			while len(bodySummary) < 180:
				bodySummary = bodySummary + sList[i]
				i = i+1

			# now save it. FIX THIS -- make it a bulked query; see notes.txt
			new = Article(
					url = url,
					title = a.title,
					source = a.domain, # actually gives www.politico.com eg
					body = a.cleaned_text,
					bodySummary = bodySummary,
					publish_date = a.publish_date,
					)
					# FIX THIS -- PARSE TAGS FOR TAGGALBEMANAGER
					# tags = a.tags, # could also add meta_keywords, difference depends on site
			artList.append(new)
	Article.objects.bulk_create(artList)

class Comment(models.Model):
	# FIX THIS this needs to be changed to current user
	author = CharField(max_length=60, blank=True)
	body = TextField()
	article = ForeignKey(Article, related_name="comments", blank=True, null=True)
	created = DateTimeField(auto_now_add=True)
	tags = TaggableManager()

	def __unicode__(self):
		return u"%s: %s" % (self.article, self.body[:60])

class Rebutt(models.Model):
	# FIX THIS this needs to be changed to current user
	author = CharField(max_length=60, blank=True)
	body = TextField()
	comment = ForeignKey(Comment, related_name="rebutts", blank=True, null=True)
	created = DateTimeField(auto_now_add=True)
	tags = TaggableManager()

	def __unicode__(self):
		return u"%s: %s" % (self.comment, self.body[:60])

class ArticleAdmin(admin.ModelAdmin):
        #list_display = []
        search_fields=["title"]

class CommentAdmin(admin.ModelAdmin):
        search_fields=["author"]

class RebuttAdmin(admin.ModelAdmin):
	search_fields=["author"]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Rebutt, RebuttAdmin)
