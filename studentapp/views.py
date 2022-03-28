from django.db.models import Sum,Avg,Max,Min,Count,F,Func
from django.shortcuts import render
from studentapp.models import Student



def StudentListView(request):
    # students_list = Student.objects.values().annotate(
    #     sum=F('subject1') + F('subject2') + F('subject3') + F('subject4') + F('subject5') + F('subject6'))

    # average = [(student['sum']/600)*100 for student in students_list]

    students_list = Student.objects.values().annotate(
        sum=F('subject1') + F('subject2') + F('subject3') + F('subject4') + F('subject5') + F('subject6'),

        avg=(F('subject1') + F('subject2') + F('subject3') + F('subject4') + F('subject5') + F('subject6')) / 600 * 100)

    context = {
        "students_list" : students_list,
    }
    return render(request,'student_list.html',context)

