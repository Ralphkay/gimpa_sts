from django.shortcuts import render
from django

# Create your views here.


def evaluation_module_view(request):
    context = {"page_title": "Evaluation Module"}
    return render(request, 'evaluation_app/evaluation_form.html', context=context)

class EvaluationModuleView(TemplateView)