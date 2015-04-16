from django import forms

GS_SUBJECTS = (
	('ECO', 'Economics'),
	('HIS', 'History'),
	('GEO', 'Geography'),
	('CLR', 'Culture and Arts'),
	('ENV', 'Environment and Ecology'),
	('SCI', 'Science and Technology'),
	('CRN', 'Current Affairs'),

BLOOM_TAG = (
	('KNO', 'Knowledge'),
	('COM', 'Comprehension'),
	('APP', 'Application'),
)

QUES_TYPES = (
	('0', 'Matching'),
	('1', 'Single Choice Correct'),
	('2', 'Two Choices Correct'),
	('3', 'Three Choices Correct'),
	('4', 'Four Choices Correct'),
)

class QuestionForm(forms.Form):
	
	ques_text = forms.CharField(max_length=1024, widget=forms.Textarea)

	ques_ch1 = forms.CharField(max_length=128)
	ques_ch2 = forms.CharField(max_length=128)
	ques_ch3 = forms.CharField(max_length=128)
	ques_ch4 = forms.CharField(max_length=128)

	ques_sub = forms.ChoiceField(widgets=forms.RadioSelect, choices=GS_SUBJECTS)
	ques_type = forms.ChoiceField(widgets=forms.RadioSelect, choices=QUES_TYPES)
	ques_bloom = forms.ChoiceField(widgets=forms.RadioSelect, choices=BLOOM_TAG)
	ques_tags = forms.CharField(widgets=forms.TextArea)
	ques_ans = forms.CharField(widgets=forms.Textarea)
	ques_dscore = forms.CharField()


