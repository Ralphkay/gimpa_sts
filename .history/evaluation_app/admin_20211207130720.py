from django.contrib import admin

# Register your models here.
from .models import Evaluation,Punctuality,Curriculum

class EvaluationAdmin(admin.ModelAdmin):
    verbose_name_plural = 'Evaluation Reports'


class Curriculum(admin.)

admin.site.register(Evaluation, EvaluationAdmin)

admin.site.register(Punctuality)
admin.site.register(Curriculum)