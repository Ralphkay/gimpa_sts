from django.urls import path

urlpatterns = [
    path('',views.evaluation_form_view,name='evaluation_form_view'),
]