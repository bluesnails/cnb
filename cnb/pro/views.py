from django.shortcuts import render

# Create your views here.

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from django.template import RequestContext

from .models import question, choice, author, tags, tagcon, answer
from .forms import QuestionForm

def index(request):
	return render(request, 'index.html')

def auth_staff(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
		    login(request, user)
		else:
		    # Return a 'disabled account' error message
			pass

	else:
	# Return an 'invalid login' error message.
		pass

#@login_required(login_url='/accounts/login/')
def add_ques(request):
	
	if request.method=='POST':
		form = QuestionForm(request.POST)
		print "here here"

		if form.is_valid():
			print "we came here"
			ques_text = form.cleaned_data['ques_text']
			ques_type = form.cleaned_data['ques_type']
			ques_dscore = form.cleaned_data['ques_dscore']
			ques_bloom = form.cleaned_data['ques_bloom']
			ques_sub  = form.cleaned_data['ques_sub']
			ques_ans = form.cleaned_data['ques_ans']
			
			ch1 = form.cleaned_data['ques_ch1']
			ch2 = form.cleaned_data['ques_ch2']
			ch3 = form.cleaned_data['ques_ch3']
			ch4 = form.cleaned_data['ques_ch4']
		
			print ques_text
			print ques_dscore
			print ques_bloom
			print ques_ans
			print ques_sub
			print ques_type

	
			ques_sol = form.cleaned_data['ques_sol']

			ques_tags = form.cleaned_data['ques_tags'].split(',')
			
			Q = question(ques_text=ques_text, 
			            ques_type=ques_type, 
			            ques_dscore=ques_dscore, 
			            ques_bloom=ques_bloom, 
			            ques_subject=ques_sub,
				    ques_author=request.user,
			     )
			Q.save()
			            
			choice1 = choice(choice_text=ch1, choice_ques=Q)
			choice1.save()
			choice2 = choice(choice_text=ch2, choice_ques=Q)
			choice2.save()
			choice3 = choice(choice_text=ch3, choice_ques=Q)
			choice3.save()
			choice4 = choice(choice_text=ch4, choice_ques=Q)
			choice4.save()		

		        ans_choice_dict = {'ch1': choice1, 'ch2': choice2, 'ch3': choice3, 'ch4':choice4}
			ans = answer(answer_text=ques_sol, answer_ques=Q, answer_choice=ans_choice[ch_ans])
			ans.save()
			
			for tag in ques_tags:
				tag = tag.strip()
				t = tags(tags_text=tag)
				t.save()
				tcon = tagcon(tagcon_tags=t, tagcon_ques=Q)
				tcon.save()
		
			print "we finally got here"	
			return HttpResponseRedirect(reverse('.views.index'))

		else:
			print "form not valid"
			print form.errors
	else:
		print "we shouldnt be here"
		form = QuestionForm()

	return render(request, 'addques.html', {'form':form})

