from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
from .forms import CreateNewList
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
"""
def index(response, name):
    ls=ToDoList.objects.get(name=name )
    item=ls.item_set.get(id=1)
    return render(response,"main/base.html",{})
"""


def index(response, id):
    ls=ToDoList.objects.get(id=id )
    if response.method == "POST":
        print(response.POST)
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete =True
                else:  
                    item.complete=False


                item.save()
        elif response.POST.get("newItem"):
            txt = response.POST.get("new")


            if len(txt) >2:
                ls.item_set.create(text=txt, complete =False)
            else:
                print("invalid")




    return render(response,"main/list.html", {"ls":ls})














def create(response):
    if response.method=="POST":
        form = CreateNewList(response.POST)


        if form.is_valid():
            n= form.cleaned_data["name"]
            t=ToDoList(name=n)
            t.save()
       
        return HttpResponseRedirect("/%i" %t.id)
   
    else:
        form =CreateNewList()
    return render(response,"main/create.html", {"form":form})






def home(response):
    return render(response,"main/home.html",{})


def demon_slayer(response):
    return render(response,"main/ds.html",{})


def demon_slayer_sc(response):
    return render(response,"main/demon_slayer_ep.html",{})


def demon_slayer_chr(response):
    return render(response,"main/demon_slayer_chr.html",{})

def opm(response):
    return render(response,"main/opm.html",{})


def black_clover(response):
    return render(response,"main/black_clover.html",{})

def dz(response):
    return render(response,"main/dz.html",{})