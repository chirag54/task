import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    test_date = models.DateTimeField('date of test')

    def __str__(self):             
        return self.question_text

    def was_test_recently(self):
	    now = timezone.now()
	    return now - datetime.timedelta(days=1) <= self.test_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    result = models.BooleanField(default=False)

    def __str__(self):            
        return self.choice_text

class Register(models.Model):
    name = models.CharField(max_length=250)
    username = models.CharField(max_length=500)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
