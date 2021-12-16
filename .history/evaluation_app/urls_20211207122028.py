from django.urls import path
from . import views
urlpatterns = [
    path('',views.EvaluationModuleView.as_view(),name='evaluation_module_view'),
]