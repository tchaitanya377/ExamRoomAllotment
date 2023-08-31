from django.db import models


# Create your models here.
Branch = (
("CSE", "CSE"),
("CSD", "CSD"),
("CSA", "CSA"),
("CSC", "CSC"),
("CST", "CST"),
("ECE", "ECE"),
("CIV", "CIV"),
("EEE", "EEE"),
("MEC", "MEC"),
)
class Student(models.Model):
    roll_Number = models.CharField(max_length=10, primary_key=True)
    branch = models.CharField(max_length=4, choices = Branch)
    year = models.IntegerField()
    Name = models.CharField(max_length=50)


class room(models.Model):
    room_number = models.CharField(max_length=6)
    seat_number = models.IntegerField()


class room_allotment(models.Model):
    roll_number = models.CharField(max_length=10)
    room_number = models.CharField(max_length=6)
    seat_number = models.IntegerField()

class RoomAllotment(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    room_number = models.IntegerField()