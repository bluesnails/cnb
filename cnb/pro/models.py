from django.db import models

from django.contrib.auth.models import User

# allow user to create quiz
class quiz(models.Model):

	quiz_id = models.AutoField(primary_key=True)
	quiz_title = models.CharField(max_length=32, blank=False)
	quiz_doc = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return self.quiz_title	

class question(models.Model):	

	ques_id = models.AutoField(primary_key=True) 
	ques_text = models.TextField(max_length=1024, blank=False)
	ques_author = models.ForeignKey('author')
	ques_created = models.DateField(auto_now_add=True)
	ques_dscore = models.IntegerField()
	ques_bloom = models.CharField(max_length=3)
	ques_subject = models.CharField(max_length=3)
	ques_type = models.CharField(max_length=1)
	ques_flags = models.CharField(max_length=16)
	ques_quiz = models.ManyToManyField('quiz')

	def __unicode__(self):
		return self.ques_text

class choice(models.Model):

	choice_id = models.AutoField(primary_key=True)
	choice_text = models.CharField(max_length=256, blank=False)
	choice_ques = models.ForeignKey('question')
#	choice_ans = models.BooleanField(default=False)
	choice_tags = models.CharField(max_length=32)

	def __unicode__(self):
		return self.choice_text

class answer(models.Model):

	answer_id = models.AutoField(primary_key=True)
	answer_text = models.TextField(max_length=1024)
	answer_ques = models.ForeignKey('question')
	answer_choice = models.ForeignKey('choice')
	answer_tags = models.CharField(max_length=128)

class author(models.Model):

	user = models.OneToOneField(User)
	domain = models.CharField(max_length=16)

	def __unicode__(self):
		return self.user.username


# a table for storing all the tags
class tags(models.Model):

	tags_id = models.AutoField(primary_key=True)
	tags_text = models.CharField(max_length=16)
	
	def __unicode__(self):
		return self.tags_text

# table that connects tags with question attached to the tag
# from all the research on the web, it can be infered that
# 3NF tagging (Toxi Solution) is the best way to go
# good for inserts but slow on selects
class tagcon(models.Model):
	
	tagcon_id = models.AutoField(primary_key=True)
	tagcon_tags = models.ForeignKey('tags')
	tagcon_ques = models.ForeignKey('question')

