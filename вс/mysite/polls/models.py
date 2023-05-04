import datetime

from django.db import models
from django.utils import timezone
from django.db import models

'''создаем модели Question и Choice
'''

class Question(models.Model):
    '''класс question имеет 2 поля'''
    '''вопрос:'''
    question_text = models.CharField(max_length=200)
    '''датa публикации:'''
    pub_date = models.DateTimeField("Дата публикации")
    
    def __str__(self):
        '''функцией str выводим именно текст вопроса, а не индекс объекта'''
        return self.question_text
    

    def was_published_recently(self):
        '''пользовательский метод; показывает дату публикации'''
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    '''класс Choice имеет 2 поля'''
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    '''выбор:'''
    choice_text = models.CharField(max_length=200)
    '''подсчет голосов:'''
    votes = models.IntegerField(default=0)

    def __str__(self):
        '''вывод текст ответа, а не индекс'''
        return self.choice_text

