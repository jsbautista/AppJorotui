from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('variables/', views.variable_list, name='variableList'),
    path('variablesj/', views.variableList, name='variableListj'),
    path('variablecreate/', csrf_exempt(views.variable_create), name='variableCreate'),
    path('variableedit/<int:variable_id>',views.variable_edit),
]
