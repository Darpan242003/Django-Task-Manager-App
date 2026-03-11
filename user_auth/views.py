from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'login.html', {'pw_mismatch': True})

    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'user_error':'True'})

        if password == confirm_password:
            user = User.objects.create(
                first_name = firstname,
                last_name = lastname,
                email = email,
                username = username
            )
            print(user)

            user.set_password(password)
            user.save()

            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'register.html', {'pw_mismatch': True})

    return render(request, 'register.html')

@login_required
def profile(request):

    return render(request, 'profile.html')

@login_required
def user_logout(request):
    logout(request)

    return redirect('login')

@login_required
def update_profile(request):

    updated_user = request.user
    if request.method == "POST":
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']

        updated_user.first_name = firstname
        updated_user.last_name = lastname
        updated_user.email = email
        updated_user.username = username
        updated_user.save()

        return redirect('profile')


    return render(request, 'update.html')

@login_required
def change_pass(request):

    user = request.user
    if request.method == "POST":
        oldpassword = request.POST['old_password']
        newpassword = request.POST['new_password']

        if user.check_password(oldpassword):
            user.set_password(newpassword)
            user.save()
            return redirect('login')
        else:
            return render(request, 'password.html', {'failed':True})

    return render(request, 'password.html')

