from django.contrib import admin
from .models import Student, Course, Subject, Mark, Tutor, Notification

# Register your models here.
# admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Subject)
#admin.site.register(Mark)
admin.site.register(Notification)


# admin.site.register(Tutor)
class StudentInline(admin.TabularInline):
    model = Student
    fields = ['name', 'adm_no', 'reg_no', 'course']


@admin.register(Tutor)
class BookAdmin(admin.ModelAdmin):
    inlines = [StudentInline]

