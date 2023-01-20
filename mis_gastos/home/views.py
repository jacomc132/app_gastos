from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required



"""Vista del home principal que une las aplicaciones billetera y ahorros"""
def home(request):
    return render(request,'home.html')


"""Vista que permite que un usuario se registre"""
def registerPage(request):
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('home:home')
        else:
            messages.error(request,"¡Error al enviar el formulario, trata con otro usuario ó contraseña!")

    
    return render(request,'register.html',{'UserCreationForm':UserCreationForm})
    



"""Vista para login y register de usuario"""
def loginPage(request):

    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request,"¡Usuario no existe!")
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect(reverse('home:home'))


        elif user == None:
            messages.error(request,"¡Clave erronea!")
    return render(request,'login.html')
        



"""Vista para logout de usuario"""
@login_required(login_url="/home/login")
def logoutPage(request):
    logout(request)
    return redirect(reverse('home:home'))



