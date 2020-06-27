from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def Index(request):
    data = UserDataBase.objects.all()
    edu_data=Education.objects.all()
    dict = {"data": data,"edu_data":edu_data}
    return render(request, "index.html", dict)


def Login(request):
    if request.user.is_authenticated:
        return redirect("userDetails")
    validation_error=False
    if request.method == "POST":
        data = request.POST
        un = data["un"]
        ps = data["ps"]
        print("un",un,"ps",ps)
        usr = authenticate(request, username=un, password=ps)
        if usr != None:
            login(request, usr)
            return redirect("index")
        validation_error=True
    dict={"validation_error":validation_error}
    return render(request, "login.html",dict)


def Logout(request):
    logout(request)
    return redirect("index")


def Add_User_Details(request):
    form = AddUser_Form()
    edu_form=Education_Form()
    if request.method == "POST":
        form = AddUser_Form(request.POST, request.FILES)
        edu_form=Education_Form(request.POST,request.FILES)
        if form.is_valid():
            data = form.save()
            return redirect("index")

    dict = {"form": form,"edu_form":edu_form}
    return render(request, "user_details_form.html", dict)



def Edit_User_Details(request):
    form=AddUser_Form()
    if request.method=="POST":
             username=request.user.username
             usr=User.objects.filter(username=username)
             Usr=usr[0]
             print("userrr is",Usr)
             user_data=UserDataBase.objects.get(usr=Usr)
             form=AddUser_Form(request.POST or None, request.FILES or None,instance=user_data)
             if form.is_valid():
                       form.save()
                       #data.usr=request.user.username
                       #data.save()
                       print("form validet")
                       return redirect("index")
    edu_form = Education_Form()
    dict={"form":form,"edu_form":edu_form}
    return render(request,"user_details_form.html",dict)