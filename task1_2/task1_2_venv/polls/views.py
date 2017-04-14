from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    # question = get_object_or_404(Question, pk=question_id)
    template_name = 'polls/detail.html'
    # return render(request, 'polls/detail.html', {'question':question})

class ResultsView(generic.DetailView):
    model = Question
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'polls/results.html', {'question': question})
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': "not select a choice",})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def find(request):
    return render(request, 'polls/find.html', {})

def input(request):
    givenurl = request.POST['givenurl']
    if givenurl=='':
        raise Http404("URL is not defined")
    else:
        print(givenurl)
        return HttpResponseRedirect(reverse('polls:output', args=(givenurl,)))

def output(request, givenurl):
    givenurl = givenurl
    return render(request, 'polls/output.html', {})
