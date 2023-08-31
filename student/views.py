from django.shortcuts import render
from .models import *
from django.views.generic import ListView
import random


# Create your views here.

def RollNumber(request):
    if request.method == 'POST':
        RollNum = request.POST.get('rollnumber')
        print(RollNum)
        # objects = Student.objects.all()
        results = Student.objects.filter(roll_Number__contains=RollNum)
        print(results)
        return render(request, 'RollAllotment.html', {'results': results})
    else:
        return render(request, 'rollnumber.html')


class students(ListView):
    model = Student
    template_name = 'studentslist.html'
    context_object_name = 'data'

class Rooms(ListView):
    model = room
    template_name = 'roomlist.html'
    context_object_name = 'data'

#
# def shuffle_and_allot_rooms(request):
#     students_by_branch_and_year = Student.objects.order_by('branch', 'year', 'roll_Number')
#     students_list = list(students_by_branch_and_year)
#     room_size = 24
#     rooms = []
#
#     for i, student in enumerate(students_list, start=1):
#         room_number = i // room_size + 1
#         room_allotmen = room_allotment(roll_number=student, room_number=room_number, seat_number=room_size)
#         room_allotmen.save()
#         rooms.append((student.roll_Number, student.branch, student.year, room_number))
#
#     return render(request, 'allotment.html', {'rooms': rooms})
def shuffle_and_allot_rooms(request):
    students_by_branch_and_year = Student.objects.order_by('branch', 'year', 'roll_Number')
    students_list = list(students_by_branch_and_year)
    room_size = 24
    rooms = []

    for i, student in enumerate(students_list, start=1):
        room_number = i // room_size + 1
        room_allotment = RoomAllotment(student=student, room_number=room_number)
        room_allotment.save()
        rooms.append((student.roll_Number, student.branch, student.year, room_number))

    return render(request, 'allotment.html', {'rooms': rooms})

def shuffle(request):
    students_roll_number = list(Student.objects.order_by('roll_Number'))
    branch_list = list(Student.objects.order_by('branch'))
    branch= random.choice(branch_list)
    room_list = room.objects.order_by('room_number')
    room_num = random.choice(room_list)
    room_size = 24
    for i, student in enumerate(students_roll_number, start=1):
        rooms = room_num
        room_size = room_size+1
        room_allot = room_allotment(roll_number=students_roll_number, room_number=room_num, seat_number=room_size)
        room_allot.save()
        return render(request, 'allotment.html', {'rooms': rooms})