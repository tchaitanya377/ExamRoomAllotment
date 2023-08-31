from django.urls import path
from . import views
from .views import students, Rooms, shuffle_and_allot_rooms, shuffle
urlpatterns = [
    path('', views.RollNumber, name = 'rollnumber'),
    path('students/', students.as_view(), name='students'),
    path('rooms/', Rooms.as_view(), name='room'),
    path('shuffle/', shuffle, name='shuffle-room-allotment'),
]