from django.contrib import admin

# Register your models here.
from .models import Evaluation,Punctuality,Curriculum

class EvaluationAdmin(admin.ModelAdmin):
    verbose_name = 'Evaluation Reports'

admin.site.register(Evaluation, EvaluationAdmin)

admin.site.register(Punctuality)
admin.site.register(Curriculum)