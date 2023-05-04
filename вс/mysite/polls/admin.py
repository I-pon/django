from django.contrib import admin

from .models import Question

'''возможность редактировать опросы админу'''
admin.site.register(Question)
# Register your models here.
