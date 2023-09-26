from django import forms
from app.models import Lesson

class LessonForm(forms.Form):
    lesson = forms.ModelChoiceField(queryset=Lesson.objects.all(),
                                    widget=forms.HiddenInput)