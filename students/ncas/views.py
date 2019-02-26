from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext
from django.views import generic
from django.views.generic import FormView

from .models import Student, Course, Subject, Mark, Notification, Assignment, Tutor
from django.contrib.auth.mixins import LoginRequiredMixin
# from .forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .forms import StudentCreation, UserCreationForm, MarkCreation, AssignmentsCreation
from django.contrib.auth.decorators import permission_required


def studentdetail(request, pk):
    std = get_object_or_404(Student, reg_no=pk)
    mrk = std.mark_set.all().order_by('sub')
    return render(request, 'ncas/studentdetails.html', {'student': std, 'mark': mrk})


@permission_required('auth.add_user')
def user_create(request):
    if request.method == "POST":
        sign = UserCreationForm(request.POST)
        if sign.is_valid():
            sign.save()
            u = sign.cleaned_data.get('username')
            p = sign.cleaned_data.get('password1')
            user = authenticate(username=u, password=p)
            return redirect('ncas:studentcreate', pk=user.id)
        else:
            return render(request, 'ncas/signup.html', {'form': sign})
    else:
        sign = UserCreationForm()
        return render(request, 'ncas/signup.html', {'form': sign})


@permission_required('auth.add_user')
def student_create(request, pk):
    if request.method == "POST":
        form = StudentCreation(request.POST)
        student = Student()
        student.details = User.objects.get(id=pk)
        student.tutor = request.user.tutor  # User.objects.get(id=request.user.id)
        if form.is_valid():
            student.name = form.cleaned_data['name']
            student.reg_no = form.cleaned_data['reg_no']
            student.adm_no = form.cleaned_data['adm_no']
            student.course = form.cleaned_data['course']
            student.save()
            return redirect('ncas:studentdetail', pk=student.pk)
        else:
            return render(request, 'ncas/studen_create.html', {'form': form})
    else:
        form = StudentCreation()
        return render(request, 'ncas/studen_create.html', {'form': form})


@permission_required('auth.add_user')
def studentlist(request):
    li = request.user.tutor.student_set.all()
    return render(request, 'ncas/studentlist.html', {'list': li})


@permission_required('auth.add_user')
def mark_update(request, pk):
    mark = get_object_or_404(Mark, uuid=pk)

    form = MarkCreation(request.POST or None, instance=mark)
    if form.is_valid():
        form.save()
        return redirect('ncas:studentdetail', pk=mark.student.pk)
    return render(request, 'ncas/mark_create.html', {'form': form})


def home(request):
    return render(request, 'ncas/home.html')


class StudentProfile(generic.DetailView):
    model = Student
    template_name = 'ncas/profiledetail.html'
    context_object_name = 'student'


class Notifs(generic.ListView):
    model = Notification
    template_name = 'ncas/notifbar.html'
    context_object_name = 'notifs'

    def get_queryset(self):
        return Notification.objects.all().order_by('-date_of_published')


class NotifsD(generic.DetailView):
    model = Notification
    template_name = 'ncas/notifs.html'
    context_object_name = 'notifsd'


def assignmentsl(request, pk):
    t = get_object_or_404(Tutor, id=pk)
    ass = t.assignment_set.all()
    return render(request, 'ncas/assignments.html', {'ass': ass})


class AssignmentsD(generic.DetailView):
    model = Assignment
    template_name = 'ncas/assd.html'
    context_object_name = 'assd'


def assc(request, pk):
    if request.method == "POST":
        form = AssignmentsCreation(request.POST)
        assi = Assignment()
        assi.tutor = Tutor.objects.get(id=pk)
        if form.is_valid():
            assi.topic = form.cleaned_data['topic']
            assi.descrip = form.cleaned_data['descrip']
            assi.sub = form.cleaned_data['sub']
            assi.last_date = form.cleaned_data['last_date']
            assi.file = form.cleaned_data['file']
            assi.save()
            return redirect('ncas:assd', pk=assi.id)
        else:
            return render(request, 'ncas/assc.html', {'form': form})
    else:
        form = AssignmentsCreation()
        return render(request, 'ncas/assc.html', {'form': form})
