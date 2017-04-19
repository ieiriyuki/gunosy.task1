from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.views import generic

import requests, sys, os
from bs4 import BeautifulSoup
from sklearn.externals import joblib
from .models import Choice, Question#, Fit

sys.path.append(os.path.abspath('naivebayes'))
from nbModel import naiveBayes

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
    #fit = Fit
    givenurl = request.POST['givenurl']
    if givenurl=='':
        raise Http404("URL is not defined")
    else:
        src = requests.get(givenurl).text
        soup = BeautifulSoup(src, 'html.parser')
        text = soup.select('h1')[0].string

        #fit.pypo()
        dir = os.path.abspath('naivebayes')
        name = 'storedmodel.pkl'
        pred = joblib.load(os.path.join(dir,name))
        call = pred.classify(pred.to_words(text))
        return render(request, 'polls/output.html', {'call':' '+call})

def output(request, text):
    data = text
    return render(request, 'polls/output.html', {})
