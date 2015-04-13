from django.shortcuts import render

# Create your views here.

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import question, choice

def auth_staff(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)

        else:
            # Return a 'disabled account' error message

    else:
        # Return an 'invalid login' error message.

@login_required(login_url='/accounts/login/')
def add_ques(request):
	return render('addquestion.html', context_instance=RequestContext(request))

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

		Q = question(ques_text=qtext, ques_type=qtype, ques_dscore=qdscore, ques_bloom=qbtag, ques_subject=qsub)
		ch1 = choice(choice_text=ch1_text, choice_ques=Q, choice_ans=ch1_ans)

	else:
		return HttpResponseRedirect(reverse('.views.add_ques'))

	return render('saved.html', context_instance=RequestContext(request))
