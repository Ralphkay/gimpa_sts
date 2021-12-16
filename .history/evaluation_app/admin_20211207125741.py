from django.contrib import admin

# Register your models here.
from .models import Evaluation,Punctuality,Curriculum

class EvaluationAdmin(admin.Admin):
    verbose_name ='Evaluation Re'

admin.site.register(Evaluation)
admin.site.register(Punctuality)
admin.site.register(Curriculum)