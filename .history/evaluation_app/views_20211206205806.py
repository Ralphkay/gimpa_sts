from django.shortcuts import render

# Create your views here.


def evaluation_form_view(request):
    context = {"eval"}
    return render(request, 'evaluation_app/evaluation_form.html')