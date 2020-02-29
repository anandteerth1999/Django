from django.shortcuts import render
from django.http import HttpResponse

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