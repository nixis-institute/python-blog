from django.shortcuts import render, HttpResponse,render_to_response,HttpResponseRedirect
from app.models import *


# Create your views here.
def home (request):
    return render_to_response("home.html")

def about (request):
    return render_to_response("about.html")

def blog_view(request):
    data=blog.objects.all()
    return render_to_response('blog_home.html',{"blog":data})

def detail_blog (request,pk):
    data=blog.objects.get(id=pk)
    return render_to_response('detail.html',{"blog":data})

def create_blog(request):
    return render(request,"create.html")


def post(request):
    t = request.POST.get('title',)
    b = request.POST.get('body',)
    e = request.POST.get('email',)
    p = request.POST.get('phone',)

    blog.objects.create(title=t,body=b,email=e,phone=p)
    

    return HttpResponseRedirect("/")
