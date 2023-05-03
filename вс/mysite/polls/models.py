import datetime

from django.db import models
from django.utils import timezone
from django.db import models

#создаем модели Question и Choice
class Question(models.Model):# имеет 2 поля
    question_text = models.CharField(max_length=200)#вопрос
    pub_date = models.DateTimeField("Дата публикации")#датa публикации
    def __str__(self):#выводим именно текст вопроса, а не индекс объекта
        return self.question_text
    def was_published_recently(self):#пользовательский метод; показывает дату публикации
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)#выбор
    votes = models.IntegerField(default=0)#подсчет голосов
    def __str__(self):
        return self.choice_text#вывод текс ответа, а не индекс 

