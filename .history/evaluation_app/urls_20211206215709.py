from django.urls import path
from . import views
urlpatterns = [
    path('',views.evaluation_module_view,name='evaluation_module_view'),
]