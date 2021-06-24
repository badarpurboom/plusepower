from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
from . models import *
# Create your views here.

@csrf_exempt
def home(request):
    if request.method=='POST':
        name=request.POST['name']
        phone=request.POST['phone']

        ins=Contact(name=name,phone=phone)
        ins.save()
        return redirect('/')
        
    
    return render(request,'home/home.html')
