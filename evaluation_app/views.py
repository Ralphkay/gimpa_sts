from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView, DetailView, View
from django.contrib import messages

from accounts.auth_decorators import allowed_groups
from accounts.models import Student
from .models import Evaluation, EvaluationSubmission, Program, Course
from .forms import EvaluationForm
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()


@login_required
@allowed_groups(permitted_groups=['student'])
def evaluations(request):
    student = get_object_or_404(Student, user=request.user.id)
    # user = User.objects.get(id=request.user.id)
    # print("student =>", user, student)
    # student = Student.objects.filter(user=request.user.id)
    courses_assigned_to_student_by_level = Course.objects.filter(program=student.program, level=student.level,
                                                                 course_group=student.course_group)
    evaluated_submissions = EvaluationSubmission.objects.filter(submitter=student).values_list('evaluationInfo')
    evaluation_set = Evaluation.objects.filter(Q(course__in=courses_assigned_to_student_by_level))\
        .exclude(id__in=evaluated_submissions)
    #
    # print(evaluation_set)
    #
    context = {'evaluations': evaluation_set, 'evaluated_submissions': evaluated_submissions, 'page_title':'Evaluations'}
    print(request.user, student, courses_assigned_to_student_by_level)
    return render(request, 'evaluation_app/evaluations.html', context)


@login_required
@allowed_groups(permitted_groups=['student'])
def evaluation_view_form(request, pk):
    evaluation_instance = get_object_or_404(Evaluation, pk=pk)
    student = get_object_or_404(Student, user=request.user)

    evaluation_form = EvaluationForm(initial={'evaluationInfo': evaluation})

    if request.method == 'POST':
        evaluation_form = EvaluationForm(request.POST, initial={'evaluationInfo': evaluation_instance,
                                                                'submitter': request.user.id})
        if evaluation_form.is_valid():
            EvaluationSubmission(submitter=student, evaluationInfo=evaluation_instance,
                                 **evaluation_form.cleaned_data).save()
            messages.success(request, f"Thank you for evaluating!")
            return redirect('evaluations')
        else:
            print(evaluation_form.errors)

    context = {'evaluation': evaluation_instance, 'evaluation_form': evaluation_form}
    return render(request, 'evaluation_app/evaluation_form.html', context)


@login_required
@allowed_groups(permitted_groups=['qasa'])
def edit_evaluation(request, pk):
    student = get_object_or_404(Student, user=request.user)
    evaluation_submission = get_object_or_404(EvaluationSubmission, pk=pk)
    # print(evaluation_instance)
    # evaluation_submission = EvaluationSubmission.objects.filter(submitter=student,
    #                                                             evaluationInfo=evaluation_instance)

    evaluation_edit_form = EvaluationForm(instance=evaluation_submission)

    context = {'page_title': 'Proceed to evaluate: ', 'evaluation_form': evaluation_edit_form,
               'working_form': evaluation_submission}

    if request.method == "POST":
        evaluation_edit_form = EvaluationForm(request.POST, instance=evaluation_submission)
        if evaluation_edit_form.is_valid():
            evaluation_edit_form.save()
            return redirect('evaluations')
    return render(request, 'evaluation_app/evaluation_form.html', context)


@login_required
@allowed_groups(permitted_groups=['student'])
def evaluation(request, slug):
    # fetch all yet to be evaluated courses filtered by student's course and submissions
    # (meaning ones he may not have submitted yet)

    # Get fresh copy of evaluation form for specific course
    evaluation_submission = get_object_or_404(EvaluationSubmission, slug=slug, submitter=None)
    # print(evaluation_submission)

    evaluation_instance = get_object_or_404(Evaluation, course=evaluation_submission.evaluationInfo.course)
    print(evaluation_instance)
    # Get instance of student
    student = get_object_or_404(Student, user=request.user)
    # Initialize evaluation form
    evaluation_form = EvaluationForm(instance=evaluation_submission,
                                     initial={'submitter': student, 'evaluationInfo': evaluation_instance})

    context = {'page_title': 'Proceed to evaluate: ', 'evaluation_form': evaluation_form,
               'working_form': evaluation_submission}

    if request.method == 'POST':
        evaluation_form = EvaluationForm(request.POST, initial={'submitter': student,
                                                                'evaluationInfo': evaluation_instance})

        if evaluation_form.is_valid():
            EvaluationSubmission(submitter=student, evaluationInfo=evaluation_instance,
                                 **evaluation_form.cleaned_data) \
                .save()
            return redirect('evaluations')
        else:
            print("errors: =>>", evaluation_form.errors)
            return render(request, 'evaluation_app/evaluation_form.html', context)

    return render(request, 'evaluation_app/evaluation_form.html', context)