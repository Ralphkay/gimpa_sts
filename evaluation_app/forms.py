from cProfile import label

from django import forms
from .models import Evaluation, FeedbackChoices, EvaluationSubmission

feedback_choices = [
    ('1', 'Poor'),
    ('2', 'Okay'),
    ('3', 'Good'),
    ('4', 'Very Good'),
    ('5', 'Excellent'),
]

"""
curriculum_feedback_beginning = models.IntegerField(choices=FeedbackChoices.choices, blank=True, null=True)
    curriculum_feedback_course = models.IntegerField(choices=FeedbackChoices.choices, blank=True, null=True)
    curriculum_feedback_lecture = models.IntegerField(choices=FeedbackChoices.choices, blank=True, null=True)
    curriculum_feedback_procedures = models.IntegerField(choices=FeedbackChoices.choices, blank=True, null=True)
    curriculum_feedback_books = 
"""


class EvaluationForm(forms.ModelForm):
    curriculum_feedback_beginning_answer = forms.ChoiceField(widget=forms.RadioSelect, choices=feedback_choices,
                                                             label="Is the curriculum well structured?")
    curriculum_feedback_course_answer = forms.ChoiceField(widget=forms.RadioSelect, choices=feedback_choices,
                                                          label="Does the lecturer gives prompt feedback?")
    curriculum_feedback_lecture_answer = forms.ChoiceField(widget=forms.RadioSelect, choices=feedback_choices,
                                                           label="Does the lecturer render good feedback?")
    curriculum_feedback_procedures_answer = forms.ChoiceField(widget=forms.RadioSelect, choices=feedback_choices,
                                                              label="Does the lecturer gives good feedback?")
    curriculum_feedback_books_answer = forms.ChoiceField(widget=forms.RadioSelect, choices=feedback_choices)

    attendance_schedule = forms.ChoiceField(widget=forms.RadioSelect, choices=feedback_choices)
    attendance_punctuality = forms.ChoiceField(widget=forms.RadioSelect, choices=feedback_choices)
    attendance_presence = forms.ChoiceField(widget=forms.RadioSelect, choices=feedback_choices)

    delivery_enthusiasm = forms.ChoiceField(widget=forms.RadioSelect, choices=feedback_choices)
    delivery_sequence = forms.ChoiceField(widget=forms.RadioSelect, choices=feedback_choices)
    delivery_organization = forms.ChoiceField(widget=forms.RadioSelect, choices=feedback_choices)
    delivery_clarity = forms.ChoiceField(widget=forms.RadioSelect, choices=feedback_choices)
    delivery_contents = forms.ChoiceField(widget=forms.RadioSelect, choices=feedback_choices)
    delivery_responsiveness = forms.ChoiceField(widget=forms.RadioSelect, choices=feedback_choices)
    delivery_achievements = forms.ChoiceField(widget=forms.RadioSelect, choices=feedback_choices)
    delivery_innovation = forms.ChoiceField(widget=forms.RadioSelect, choices=feedback_choices)
    delivery_theory_practices = forms.ChoiceField(widget=forms.RadioSelect, choices=feedback_choices)

    assignments_relevance = forms.ChoiceField(widget=forms.RadioSelect, choices=feedback_choices)
    assignments_promptitude = forms.ChoiceField(widget=forms.RadioSelect, choices=feedback_choices)
    assignments_feedback = forms.ChoiceField(widget=forms.RadioSelect, choices=feedback_choices)
    assignments_guidance = forms.ChoiceField(widget=forms.RadioSelect, choices=feedback_choices)

    interaction_availability = forms.ChoiceField(widget=forms.RadioSelect, choices=feedback_choices)
    interaction_help = forms.ChoiceField(widget=forms.RadioSelect, choices=feedback_choices)
    interaction_fairness = forms.ChoiceField(widget=forms.RadioSelect, choices=feedback_choices)

    environment_classroom_size = forms.ChoiceField(widget=forms.RadioSelect, choices=feedback_choices)
    environment_seats = forms.ChoiceField(widget=forms.RadioSelect, choices=feedback_choices)
    environment_audio_visual_equip = forms.ChoiceField(widget=forms.RadioSelect, choices=feedback_choices)
    environment_public_address = forms.ChoiceField(widget=forms.RadioSelect, choices=feedback_choices)
    environment_books = forms.ChoiceField(widget=forms.RadioSelect, choices=feedback_choices)
    environment_computers = forms.ChoiceField(widget=forms.RadioSelect, choices=feedback_choices)
    environment_internet = forms.ChoiceField(widget=forms.RadioSelect, choices=feedback_choices)
    environment_air_conditioning = forms.ChoiceField(widget=forms.RadioSelect, choices=feedback_choices)
    environment_secretariat = forms.ChoiceField(widget=forms.RadioSelect, choices=feedback_choices)

    is_evaluated = forms.BooleanField()

    # submitter = forms.CharField(widget=forms.HiddenInput)

    class Meta:
        model = EvaluationSubmission
        fields = ["curriculum_feedback_beginning_answer",
                  'curriculum_feedback_course_answer',
                  'curriculum_feedback_lecture_answer',
                  "curriculum_feedback_procedures_answer",
                  "curriculum_feedback_books_answer",

                  "attendance_schedule",
                  "attendance_punctuality",
                  "attendance_presence",

                  "delivery_enthusiasm",
                  "delivery_sequence",
                  "delivery_organization",
                  "delivery_clarity",
                  "delivery_contents",
                  "delivery_responsiveness",
                  "delivery_achievements",
                  "delivery_innovation",
                  "delivery_theory_practices",

                  "assignments_relevance",
                  "assignments_promptitude",
                  "assignments_feedback",
                  "assignments_guidance",

                  "interaction_availability",
                  "interaction_help",
                  "interaction_fairness",

                  "environment_classroom_size",
                  "environment_seats",
                  "environment_audio_visual_equip",
                  "environment_public_address",
                  "environment_books",
                  "environment_computers",
                  "environment_internet",
                  "environment_air_conditioning",
                  "environment_secretariat",

                  "is_evaluated",

                  # "submitter"

                  ]

    # def save(self, commit=True, *args, **kwargs):
    #     # obj = super(EvaluationForm, self).save(commit=False, *args, **kwargs)
    #     # print(f"{obj.curriculum_feedback_beginning} something good")
    #     if commit:
    #         obj.save()

    # class Meta:
    #     model = Evaluation
    #     fields = ['curriculum_feedback_beginning', 'curriculum_feedback_course', 'curriculum_feedback_lecture',
    #               'curriculum_feedback_procedures', 'curriculum_feedback_books']
    #
    #     widgets = {
    #         'curriculum_feedback_beginning': forms.RadioSelect(attrs={'class': 'n-chk new-control new-radio'}),
    #     }
