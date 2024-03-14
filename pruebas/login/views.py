from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

#def hello(request):
    #return HttpResponse("<h1>coyol</h1>")
    
def index(request):
   
    return render(request,'login/index.html')
 