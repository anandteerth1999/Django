from django.conf.urls import include, url
from django.urls import path
from myapp import views
urlpatterns= [
    path('hello/',views.hello,name='hello'),
    path('morning/',views.morning,name='morning'),
    path('article/',views.viewArticle),
]