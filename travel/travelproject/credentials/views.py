from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.shortcuts import redirect


# Create your views here.


def login(requset):
    if requset.method == 'POST':
        usern = requset.POST['un']
        password = requset.POST['pw']
        user=auth.authenticate(username = usern,password=password)

        if user is not None:
            auth.login(requset,user)
            return redirect('/')
        else:
            messages.info("invalid user or pass word")
            return redirect('login')
    return render(requset, 'login.html')




def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['pass1']
        password2 = request.POST['pass2']
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already exists")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save();
                return redirect('login')

        else:
            print("incorrect password")
            messages.info(request,"password not match")
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('login')