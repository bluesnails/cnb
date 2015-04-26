from django import forms

GS_SUBJECTS = (
	('ECO', 'Economics'),
	('HIS', 'History'),
	('GEO', 'Geography'),
	('CUL', 'Culture and Arts'),
	('ENV', 'Environment and Ecology'),
	('SCI', 'Science and Technology'),
	('CRR', 'Current Affairs'),
)

BTAX = (
	('KNO', 'Knowledge'),
	('COM', 'Comprehension'),
	('APP', 'Application'),
)

QUES_TYPES = (
	('1', 'Single Choice Correct'),
	('2', 'Two Choices Correct'),
	('3', 'Three Choices Correct'),
	('4', 'More than Three Correct'),
	('5', 'Matching'),
)

ANS_CHOICE = (
    ('ch1', 'Choice A'),
    ('ch2', 'Choice B'),
    ('ch3', 'Choice C'),
    ('ch4', 'Choice D'),
)



class QuestionForm(forms.Form):
	
	ques_text = forms.CharField(max_length=512, 
			widget=forms.Textarea(attrs={'cols': 40, 'rows': 14, 'placeholder': 'Question goes here'}))

	ques_ch1 = forms.CharField(max_length=128, 
			widget=forms.Textarea(attrs={'cols': 40, 'rows': 2, 'placeholder':'Choice A'}))

	ques_ch2 = forms.CharField(max_length=128, 
			widget=forms.Textarea(attrs={'cols': 40, 'rows': 2, 'placeholder':'Choice B'}))

	ques_ch3 = forms.CharField(max_length=128, 
			widget=forms.Textarea(attrs={'cols': 40, 'rows': 2, 'placeholder':'Choice C'}))

	ques_ch4 = forms.CharField(max_length=128, 
			widget=forms.Textarea(attrs={'cols': 40, 'rows': 2, 'placeholder':'Choice D'}))


	ques_sub = forms.ChoiceField(widget=forms.RadioSelect, choices=GS_SUBJECTS)

	ques_type = forms.ChoiceField(widget=forms.RadioSelect, choices=QUES_TYPES)

	ques_bloom = forms.ChoiceField(widget=forms.RadioSelect, choices=BTAX)

	ques_tags = forms.CharField(max_length=128, 
			widget=forms.Textarea(attrs={'rows': 4, 'placeholder':'Comma-separated tags'}))

	ques_ans = forms.ChoiceField(widget=forms.RadioSelect, choices=ANS_CHOICE)

	ques_sol = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 14, 'placeholder':'Optional: solution'}))
	ques_dscore = forms.IntegerField(max_length=1, 
				widget=forms.TextInput(attrs={'placeholder':'1-10'}))

