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

QUES_TYPES = (
	('0': 'Matching'),
	('1': 'Single Choice Correct'),
	('2': 'Two Choices Correct'),
	('3': 'Three Choices Correct'),
	('4': 'Four Choices Correct'),
)

class question(models.Model):

	ques_id = models.AutoField(primary_key=True) 
	ques_text = models.TextField(max_length=1024)
	ques_author = models.ForeignKey('author')
	ques_created = models.DateField(auto_add_now=True)
	ques_dscore = models.IntegerField()
	ques_bloom = models.CharField(max_length=3, choices=BLOOM_TAG)
	ques_subject = models.CharField(max_length=3, choices=GS_SUBJECTS)
	ques_type = models.CharField(max_length=1, choices=QUES_TYPES)
	ques_flags = models.CharField(max_length=16)

	def __unicode__(self):
		return self.ques_text

class choice(models.Model):

	choice_id = models.AutoField(primary_key=True)
	choice_text = models.CharField(max_length=128)
	choice_ques = models.ForeignKey('question')
	choice_ans = models.BooleanField(default=False)
	choice_mtags = models.CharField(max_length=32)

	def __unicode__(self):
		return self.choice_text

class author(models.Model):
	
	auth_id = models.AutoField(primary_key=True)	
	auth_username = models.CharField(max_length=32)
	auth_doj = models.DateField(auto_add_now=True)
	auth_org = models.CharField(max_length=32)
	auth_email = models.EmailField()

	def __unicode__(self):
		return self.author_username

class author_tags(models.Model):

	atags_id = models.AutoField(primary_key=True)
	atags_text = models.CharField(max_length=16)
	
	def __unicode__(self):
		return self.atags_text

class acon(models.Model):

	acon_id = models.AutoField(primary_key=True)
	acon_atag = models.ForeignKey('author_tags')
	acon_ques = models.ForeignKey('question')

class machine_tags(models.Model):

	mtags_id = models.AutoField(primary_key=True)
	mtags_text = models.CharField(max_length=16)

	def __unicode__(self):
		return self.mtags_text

class mcon(models.Model):

	mcon_id = models.AutoField(primary_key=True)
	mcon_mtag = models.ForeignKey('machcine_tags')
	mcon_ques = models.ForeignKey('qustion')
