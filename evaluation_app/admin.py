from django.contrib import admin

# Register your models here.
from .models import Evaluation, Facilitator, School, Program, Course, Department,EvaluationSubmission

class EvaluationAdmin(admin.ModelAdmin):
    list_display = ['course','facilitator']
    list_filter = ['course','facilitator']

    prepopulated_fields = {'slug':['course']}

admin.site.register(Evaluation)
admin.site.register(EvaluationSubmission)
admin.site.register(School)
admin.site.register(Course)
admin.site.register(Program)
admin.site.register(Facilitator)


admin.site.register(Department)
admin.site.site_header = "GIMPA STS ADMIN"
admin.site.site_title = "GIMPA STS Admin Portal"
admin.site.index_title = "Welcome to GIMPA STS Portal"


