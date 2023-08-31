# Generated by Django 4.2.4 on 2023-08-29 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_student_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='room_allotment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_number', models.CharField(max_length=10)),
                ('room_number', models.CharField(max_length=6)),
                ('seat_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RoomAllotment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='room_alloment',
        ),
        migrations.AlterField(
            model_name='room',
            name='seat_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.CharField(choices=[('CSE', 'CSE'), ('CSD', 'CSD'), ('CSA', 'CSA'), ('CSC', 'CSC'), ('CST', 'CST'), ('ECE', 'ECE'), ('CIV', 'CIV'), ('EEE', 'EEE'), ('MEC', 'MEC')], max_length=4),
        ),
        migrations.AlterField(
            model_name='student',
            name='year',
            field=models.IntegerField(),
        ),
        migrations.AddField(
            model_name='roomallotment',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='student.student'),
        ),
    ]
