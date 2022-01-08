from django.shortcuts import render
def student_details(request):
    return render(request,'Student/student_details.html')