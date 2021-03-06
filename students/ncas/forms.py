from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student, Course, Mark, Assignment


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        help_texts = {
            'username': '',
            'email': '',
            'password1': '',
            'password2': '',
        }


class StudentCreation(forms.ModelForm):
    course = forms.ModelChoiceField(queryset=Course.objects.all())

    class Meta:
        model = Student
        fields = ('name', 'adm_no', 'reg_no', 'add_ress', 'phno', 'course')


class MarkCreation(forms.ModelForm):
    class Meta:
        model = Mark
        fields = ('s_mark1', 's_mark2', 'assmnt_mark1', 'assmnt_mark2', 'attndnc_mark')


class AssignmentsCreation(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ('topic', 'descrip', 'sub', 'last_date', 'file')
