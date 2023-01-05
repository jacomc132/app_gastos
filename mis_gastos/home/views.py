from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout



"""Vista del home principal que une las aplicaciones billetera y ahorros"""
def home(request):
    return render(request,'home.html')


"""Vista que permite que un usuario se registre"""
def registerPage(request):
    if request.method == "GET":
        return render(request,'register.html')


    if request.method == "POST":
        usuario = request.POST.get("username")
        password = request.POST.get("password")

    try:
        pass
    except:
        pass



"""Vista para login y register de usuario"""
def loginPage(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request,"¡Usuario no existe!")
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect(reverse('home'))


        elif user == None:
            messages.error(request,"¡Clave erronea!")
    return render(request,'login.html')
        



"""Vista para logout de usuario"""
def logoutPage(request):
    logout(request)
    return redirect(reverse('home'))



