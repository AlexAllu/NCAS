from django.urls import path


from . import views

app_name = 'ncas'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('mark-create/<pk>', views.mark_update, name='markcreate'),
    path('user-create/', views.user_create, name='usercreate'),
    path('student-create/<int:pk>/', views.student_create, name='studentcreate'),
    path('studentlist/', views.studentlist, name='studentlist'),
    path('studentdetail/<int:pk>/', views.StudentDetail.as_view(), name='studentdetail'),
    path('notifs/', views.Notifs.as_view(), name='notifs'),
    path('notifsd/<int:pk>/', views.NotifsD.as_view(), name='notifsd'),
    path('assl/<int:pk>/', views.assignmentsl, name='assl'),
    path('assd/<int:pk>/', views.AssignmentsD.as_view(), name='assd'),
    path('assc/<int:pk>/', views.assc, name='assc')
]
