#конфигурация url для вызова сообщений
from django.urls import path

from . import views
app_name = "polls"#добавляем пространства имен, чтобы джанго знал,
                  #куда смотреть при использовании тега шаблона
#ниже подключаем вызов сообщений, в зависимости от места, где находимся
urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]