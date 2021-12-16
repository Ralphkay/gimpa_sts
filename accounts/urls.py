from django.urls import path

from .views import login_student,logout_student
urlpatterns = [
    path('login-student/', login_student, name="login_student"),
    path('logout-student/', logout_student, name="logout_student"),
    # path('register/', register, name="register"),
]