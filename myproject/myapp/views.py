from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from myapp.models import Student

# Create your views here.
def hello(request):
    text="<h1>Welcome to my app</h1>"
    return HttpResponse(text)

def morning(request):
    return HttpResponse("<h3>Good Morning</h3>")

def viewArticle(request):
    articleId = 0
    try:
        articleId = request.GET['articleId']
    except:
        pass
    return render(request,'index.html',{"articleId":articleId})

class getStudents(APIView):
    def get(self,request):
        students = Student.objects.all()
        result = []
        for stud in students: 
            result.append({
                "Name": stud.Name,
                "USN": stud.USN,
                "Class": stud.Class,
                "Section": stud.Section
            })

        return Response(result)

class getStudent(APIView):
    def get(self,request):
        usn = request.query_params['USN']
        student = Student.objects.filter(USN=usn)
        student = student[0]
        return Response({
                "Name": student.Name,
                "USN": student.USN,
                "Class": student.Class,
                "Section": student.Section
        })