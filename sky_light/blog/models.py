from django.db.models import * 
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.core.mail import send_mail
from taggit.managers import TaggableManager

class Article(models.Model):
	#this needs to be changed ot the current user
	title = CharField(max_length=60)
	author = CharField(max_length=60)
	source = CharField(max_length=60)
	body = TextField()
	upvotes = IntegerField(default=0)
	downvotes = IntegerField(default=0)
	created = DateTimeField(auto_now_add=True)
	tags = TaggableManager()
	#url


	class Meta:
		ordering = ["upvotes"]

	def __unicode__(self):
		return self.title

class Comment(models.Model):
	#this needs to be changed to current user
	author = CharField(max_length=60, blank=True)
	body = TextField()
	article = ForeignKey(Article, related_name="comments", blank=True, null=True)
	created = DateTimeField(auto_now_add=True)
	tags = TaggableManager()

	def __unicode__(self):
		return u"%s: %s" % (self.article, self.body[:60])

class Rebutt(models.Model):
	#this needs to be changed to current user
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
