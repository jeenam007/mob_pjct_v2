from django.shortcuts import render, redirect
from django.http import HttpResponse
from mobileapp.forms import ProductCreateForm
from .models import Mobile
from .forms import Mobile

# Create your views here.
def home(request):
    return HttpResponse("<h1>Home Page</h1>")

def create_product(request):
    if request.method=="GET":
        form=ProductCreateForm()
        return render(request,'create.html',{'form':form})
    
    elif request.method=="POST":
        form=ProductCreateForm(request.POST,files=request.FILES)

    if form.is_valid():
        form.save()
        return redirect('list')
    else:
         return render(request,'create.html',{'form':form})

def list_Products(request):
    pdt=Mobile.objects.all()
    context={'pdt':pdt}
    return render(request,'list.html',context)

def deletepdt(request,id):
    instance=Mobile.objects.get(id=id)
    instance.delete()
    return redirect('list')

