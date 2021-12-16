from django.contrib import admin

# Register your models here.
from .models import Evaluation,Punctuality,Curriculum

class EvaluationAdmin(admin.ModelAdmin):
    verbose_name_plural = 'Evaluation Reports'


class CurriculumAdmin(admin.ModelAdmin):
    list_display = ('feedback_1','feedback_2','feedback_3','feedback_4','feedback_5','computed')

admin.site.register(Evaluation, EvaluationAdmin)

admin.site.register(Punctuality)
admin.site.register(Curriculum)