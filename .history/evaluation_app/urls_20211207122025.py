from django.urls import path
from . import views
urlpatterns = [
    path('',views.E,name='evaluation_module_view'),
]