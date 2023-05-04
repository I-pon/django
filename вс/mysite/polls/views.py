'''здесь, в зависимости от действий,
вызываются различные сообщения'''
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"
'''def index(request):#выводит последние 5 вопросов через запятую
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)#шаблон

def detail(request, question_id):#показывает вопрос или выводит ошибку 404
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):#показывает результаты
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})
'''
def vote(request, question_id):
    '''реализуем возможность отвечать на вопрос'''
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
        '''#request.POST— это объект, похожий на словарь, 
        который позволяет вам получать доступ к отправленным
        данным по имени ключа. В этом случае request.POST['choice']возвращает
        идентификатор выбранного варианта в виде строки. 
        request.POSTзначения всегда являются строками.'''
    except (KeyError, Choice.DoesNotExist):
        '''Ответ не выбран - показываем вопрос заново'''
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        ''' Always return an HttpResponseRedirect after successfully dealing
        with POST data. This prevents data from being posted twice if a
        user hits the Back button.'''
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))