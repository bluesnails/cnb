
from django.db import models
from django.contrib.auth.models import User

from taggit.managers import TaggableManager

class Quiz(models.Model):

	title = models.CharField(max_length=32, blank=False)
	doc = models.DateField(auto_now_add=True)
	creator = models.OneToOneField(User)
	

	def __unicode__(self):
		return u'%s' % (self.title)

class Question(models.Model):	

	text = models.TextField(max_length=512, blank=False)
	author = models.ForeignKey('Author')
	doc = models.DateField(auto_now_add=True)
	dom = models.DateField(auto_now=True)
	dscore = models.IntegerField()
	btax = models.CharField(max_length=3)
	subj = models.CharField(max_length=3)
	qtype = models.CharField(max_length=1)
	flag = models.CharField(max_length=16)
	tags = TaggableManager()
	quiz = models.ForeignKey('Quiz')

	def __unicode__(self):
		return u'%s' % (self.text)

class Choice(models.Model):
	
	text = models.CharField(max_length=64, blank=False)
	ques = models.ForeignKey('Question')
	tags = TaggableManager()

	def __unicode__(self):
		return u'%s' % (self.text)

class Answer(models.Model):

	text = models.TextField(max_length=512)
	ques = models.ForeignKey('Question')
	choice = models.ForeignKey('Choice')
	tags = models.CharField(max_length=32)

	def __unicode__(self):
		return u'%s' % (self.text)

class Author(models.Model):

	user = models.OneToOneField(User)
	doj = models.DateField(auto_now_add=True)
	subj = models.CharField(max_length=16)

	def __unicode__(self):
		return u'%s' % (self.user.username)	

class Aspirant(models.Model):
	
	user = models.OneToOneField(User)
	doj = models.DateField(auto_now_add=True)
	
	def __unicode__(self):
		return u'%s' % (self.user.username)
