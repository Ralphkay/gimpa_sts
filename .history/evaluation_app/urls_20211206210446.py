from django.urls import path
from . import views
urlpatterns = [
    path('',views.evaluation_form_view,name='evaluation_form_view'),
]