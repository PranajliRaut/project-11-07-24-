
from django.shortcuts import render,redirect
from .models import Person
from .forms import PersonForm
# Create your views here.
def hview(request):
    return render(request,"app1/home.html",{})



def pview(request):
    form =PersonForm()
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/a1/sv/")
    return render(request,"app1/person_form.html",{"form":form})

def sview(request):
    per= Person.objects.all()
    print(per)
    return render(request,"app1/show.html",{"obj":per})

def uview(request,pk):
    obj = Person.objects.get(pid=pk)
    form = PersonForm(instance=obj)
    if request.method == "POST":
        form = PersonForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("/a1/sv/")
    return render(request,"app1/person_form.html",{"form":form})

def dview(request,x):
    obj =Person.objects.get(pid=x)
    obj.delete()
    return redirect("/a1/sv/")
    return render(request,"app1/person_form.html",{"obj":obj})




