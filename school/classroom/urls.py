from django.urls import path
from classroom.views import HomeView
from classroom.views import ThankYouView
from classroom.views import ContactFormView
from classroom.views import TeacherCreateView
from classroom.views import TeacherListView
from classroom.views import TeacherDetailView
from classroom.views import TeacherUpdateView
from classroom.views import TeacherDeleteView

app_name = 'classroom'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('thank_you/', ThankYouView.as_view(), name='thank_you'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('create_teacher/', TeacherCreateView.as_view(), name='create_teacher'),
    path('list_teachers/', TeacherListView.as_view(), name='list_teachers'),
    path('teacher_detail/<int:pk>', TeacherDetailView.as_view(), name='detail_teacher'),
    path('teacher_update/<int:pk>', TeacherUpdateView.as_view(), name='update_teacher'),
    path('teacher_delete/<int:pk>', TeacherDeleteView.as_view(), name='delete_teacher'),
]