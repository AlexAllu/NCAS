from django.contrib import admin
from .models import Student, Course, Subject, Mark, Tutor, Notification, Assignment

# Register your models here.
# admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Assignment)
admin.site.register(Notification)
admin.site.register(Mark)


# admin.site.register(Tutor)
class StudentInline(admin.TabularInline):
    model = Student
    fields = ['name', 'adm_no', 'reg_no', 'course']


@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    inlines = [StudentInline]


class MarkInline(admin.TabularInline):
    model = Mark
    fields = ['sub', 's_mark1', 's_mark2']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = [MarkInline]
