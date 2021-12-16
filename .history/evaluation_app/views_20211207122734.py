from django.shortcuts import render
from django.views.generic import TemplateView, ListView

# Create your views here.


class EvaluationModuleView(ListView):
    template_name = 'evaluation_app/evaluation_form.html'
    model = EvaluationModule
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Evaluation Module"
        return context