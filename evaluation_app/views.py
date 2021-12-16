from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView, DetailView, View

from accounts.models import Student
from .models import Evaluation, EvaluationSubmission, Program, Course
from .forms import EvaluationForm


# Create your views here.


@login_required
def evaluations(request):
    all_evaluations = Evaluation.objects.all().count()

    # 1. fetch non-submitted evaluations related to student
    student = get_object_or_404(Student, user=request.user)

    courses_assigned_to_student_by_level = Course.objects.filter(program=student.program, level=student.level)
    submitted_evaluated_forms_by_student = EvaluationSubmission.objects.filter(submitter=student, is_evaluated=True)
    courses = Course.objects.all()
    ids_of_courses_evaluated_by_student = []

    for submitted_form in submitted_evaluated_forms_by_student:
        for course in courses:
            if course.name == submitted_form.evaluationInfo.course.name:
                ids_of_courses_evaluated_by_student.append(course.id)

    # filtered_evaluations = Evaluation.objects.filter(~Q(course__in=courses_assigned_to_student_by_level))
    evaluation_submissions = Evaluation.objects.filter(Q(course__in=courses_assigned_to_student_by_level)). \
        exclude(course__in=ids_of_courses_evaluated_by_student)

    # fetch submitted evaluations by students, mark them as only editable
    # evaluation_forms_specific_to_student_not_evaluated = EvaluationSubmission.objects.filter(
    #     Q(evaluationInfo__in=evaluation_submissions),
    #     is_evaluated=False)
    evaluation_forms_specific_to_student_not_evaluated = EvaluationSubmission.objects.filter(
        Q(evaluationInfo__in=evaluation_submissions),
        is_evaluated=False)

    print(evaluation_forms_specific_to_student_not_evaluated)

    # print(submitted_evaluated_forms_by_student)
    # non_submitted = []
    # for e in evaluation_forms_specific_to_student_not_evaluated:
    #     if e.evaluationInfo.course.name not in submitted_evaluated_forms_by_student:
    #         non_submitted.append(e)
    #
    # print(non_submitted)


    context = {'page_title': 'Evaluation Module', 'available_evaluations': all_evaluations,
               'evaluation_forms_specific_to_student_not_evaluated': evaluation_forms_specific_to_student_not_evaluated,
               "submitted_evaluated_forms_by_student": submitted_evaluated_forms_by_student}

    return render(request, 'evaluation_app/evaluations.html', context)


@login_required
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
    print(student)
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
