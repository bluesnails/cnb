from django.db import models

# Create your models here.

GS_SUBJECTS = (
	('ECO': 'Economics'),
	('HIS': 'History'),
	('GEO': 'Geography'),
	('CLR': 'Culture and Arts'),
	('ENV': 'Environment and Ecology')
	('SCI': 'Science and Technology'),
	('CRN': 'Current Affairs'),
)

BLOOM_TAG = (
	('KNO': 'Knowledge'),
	('COM': 'Comprehension'),
	('APP': 'Application'),
)

class question(models.Model):

	ques_id = models.AutoField(primary_key=True) 
	ques_text = models.TextField(max_length=1024)
	ques_auth = models.ForeignKey('author')
	ques_doc = models.DateField(auto_add_now=True)
	ques_dscore = models.IntegerField()
	ques_bloom = models.CharField(max_length=3, choices=BLOOM_TAG)
	ques_subject = models.CharField(max_length=3, choices=GS_SUBJECTS)
	ques_atags = models.CharField(max_length=32)
	ques_mtags = models.CharField(max_length=32)

	def __unicode__(self):
		return self.ques_text

class choices(models.Model):

	choice_id = models.AutoField(primary_key=True)
	choice_text = models.CharField(max_length=128)
	choice_ques = models.ForeignKey('question')
	choice_ans = models.BooleanField(default=False)
	choice_mtags = models.CharField(max_length=32)

	def __unicode__(self):
		return self.choice_text

class author(models.Model):

	
	author_name = models.CharField(max_length=32)
	author_doj = models.DateField(auto_add_now=True)
	author_org = models.CharField(max_length=32)
	author_email = models.EmailField()

	def __unicode__(self):
		return self.author_name
