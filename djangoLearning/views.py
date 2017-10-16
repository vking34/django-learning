from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.template import Template, Context
from django.template.loader import get_template

def index(request):
    # response = HttpResponse()
    # response.write("<h1>Welcome to my website !</h1>")
    # response.write("<p>This is website created by VKing34</p>")
    # # response.write("<a href="/polls/">Click here</a><a> to get some polls.</a>")

    fp = open('/root/PycharmProjects/djangoLearning/djangoLearning/index.html')
    t = Template(fp.read())
    fp.close()
    html = t.render(Context())


    return HttpResponse(html)