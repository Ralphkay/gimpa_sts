from django.shortcuts import render

# Create your views here.


def evaluation_form_view(request):m
    context = {"evaluation_for"}
    return render(request, 'evaluation_app/evaluation_form.html')