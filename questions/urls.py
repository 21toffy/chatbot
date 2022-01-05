
from django.urls import path
from .views import *

app_name = 'questions'

urlpatterns = [
    path('stage/<int:stage_id>/',Stage1Views.as_view()),

]
