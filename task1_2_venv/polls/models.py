import datetime, sys, os

from django.db import models
from django.utils import timezone

from sklearn.externals import joblib

sys.path.append(os.path.abspath('polls/naivebayes'))
from .nbModel import naiveBayes


# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Fit():
    dir = os.path.abspath('polls/naivebayes')
    name = 'storedmodel.pkl'

    def __init__(self):
        self.model = joblib.load(os.path.join(dir,name))

    def loadmodel():
        return self.model
