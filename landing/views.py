
from django.shortcuts import render
from .models import Post

from django.template import loader 
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import get_object_or_404, render 
from django.urls import reverse 
from django.contrib.auth.decorators import login_required

from .models import Question, Choice 

def home(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5] 
	context = {'latest_question_list': latest_question_list} 
	return render(request, 'landing/home.html', context)


def about(request):
    return render(request, 'landing/about.html', {'title': 'About'})


# Get questions and display them 



 

# Show specific question and choices 


def detail(request, question_id): 
	try: 
		question = Question.objects.get(pk = question_id) 
	except Question.DoesNotExist: 
		raise Http404("Question does not exist") 
	return render(request, 'landing/detail.html', {'question': question}) 

# Get question and display results 


def results(request, question_id): 
	question = get_object_or_404(Question, pk = question_id) 
	return render(request, 'landing/results.html', {'question': question}) 

# Vote for a question choice 

@login_required
def vote(request, question_id): 
	# print(request.POST['choice']) 
	question = get_object_or_404(Question, pk = question_id) 
	try: 
		selected_choice = question.choice_set.get(pk = request.POST['choice']) 
	except (KeyError, Choice.DoesNotExist): 
		# Redisplay the question voting form. 
		return render(request, 'landing/detail.html', { 
			'question': question, 
			'error_message': "You didn't select a choice.", 
		}) 
	else: 
		selected_choice.votes += 1
		selected_choice.save() 
		# Always return an HttpResponseRedirect after successfully dealing 
		# with POST data. This prevents data from being posted twice if a 
		# user hits the Back button. 
		return HttpResponseRedirect(reverse('landing:results', args =(question.id, ))) 
