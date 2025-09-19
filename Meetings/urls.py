from django.urls import path
from . import views

urlpatterns = [
    path('new/',views.NewMeetingView.as_view()),
    path('all/',views.MeetingListView.as_view()),
] 