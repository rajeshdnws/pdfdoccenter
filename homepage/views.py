from django.shortcuts import render
import datetime  
from django.template import loader  

# Create your views here.
from django.http import HttpResponse  
  
def hello(request):  
    return HttpResponse("<h2>Hello, Welcome to Django!</h2>")  


def index(request):  
    now = datetime.datetime.now()  
    name={
        'user':'Rajesh',
         'date':now
    }
    template = loader.get_template('home.html') # getting our template  
    return HttpResponse(template.render(name))  

def about(request):  
    now = datetime.datetime.now()  
    name={
        'user':'about us pdfdoccenter',
         'date':now
    }
    template = loader.get_template('about.html') # getting our template  
    return HttpResponse(template.render(name))  
def portfolio(request):  
    now = datetime.datetime.now()  
    name={
        'title':'portfolio us pdfdoccenter',
         'date':now
    }
    template = loader.get_template('portfolio.html') # getting our template  
    return HttpResponse(template.render(name))  
def portfoliodetails(request):  
    now = datetime.datetime.now()  
    name={
        'title':'about us pdfdoccenter',
         'date':now
    }
    template = loader.get_template('portfolio-details.html') # getting our template  
    return HttpResponse(template.render(name))  
def services(request):  
    now = datetime.datetime.now()  
    name={
        'title':'service us pdfdoccenter',
         'date':now
    }
    template = loader.get_template('services.html') # getting our template  
    return HttpResponse(template.render(name))  
def resume(request):  
    now = datetime.datetime.now()  
    name={
        'title':'resume us pdfdoccenter',
         'date':now
    }
    template = loader.get_template('resume.html') # getting our template  
    return HttpResponse(template.render(name)) 
def contact(request):  
    now = datetime.datetime.now()  
    name={
        'title':'contact us pdfdoccenter',
         'date':now
    }
    template = loader.get_template('contact.html') # getting our template  
    return HttpResponse(template.render(name))  
