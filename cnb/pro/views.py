from django.shortcuts import render

# Create your views here.

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from django.template import RequestContext

from .models import question, choice, author, tags, tagcon, answer


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

@login_required(login_url='/accounts/login/')
def add_ques(request):
	return render(request, 'addques.html')

@login_required(login_url='/accounts/login/')
def save_ques(request):

	if request.method=='POST':
		qtext = request.POST['ques_text']
		qtype = request.POST['ques_type']
		qdscore = request.POST['ques_dscore']
		qbtag = request.POST['ques_btag']
		qsub  = request.POST['ques_sub']
		
		ch1 = request.POST['ch1_text']
		ch2 = request.POST['ch2_text']
		ch3 = request.POST['ch3_text']
		ch4 = request.POST['ch4_text']

		# generate mtags
		qatags = get_author_tags(request.POST['ques_atags'])

		Q = question(ques_text=qtext, ques_type=qtype, ques_dscore=qdscore, ques_bloom=qbtag, ques_subject=qsub)
		ch1 = choice(choice_text=ch1_text, choice_ques=Q, choice_ans=ch1_ans)
		ch2 = choice(choice_text=ch2_text, choice_ques=Q, choice_ans=ch2_ans)
		ch3 = choice(choice_text=ch3_text, choice_ques=Q, choice_ans=ch3_ans)
		ch4 = choice(choice_text=ch4_text, choice_ques=Q, choice_ans=ch4_ans)

		Q.save()
		ch1.save()
		ch2.save()
		ch3.save()
		ch4.save()

	else:
		return HttpResponseRedirect(reverse('.views.add_ques'))

	return render('saved.html', context_instance=RequestContext(request))
