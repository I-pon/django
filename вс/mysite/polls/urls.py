'''конфигурация url для вызова сообщений'''
from django.urls import path

from . import views

'''добавляем пространства имен, чтобы джанго знал,
куда смотреть, при использовании тега шаблона:'''
app_name = "polls" 


'''подключаем вызов сообщений, в зависимости от места, где находимся'''
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]