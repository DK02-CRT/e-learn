from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def signin (request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # print(username)
        # print(password)

        user = authenticate(
            request,
            username = username,
            password = password
        )

        if user is not None:
            login(request, user)
            return redirect("home")
        
        return render(
            request, 
            "users/signin.html",
            {"error":" Zły login lub hasło"}
        )
    return render(request, "users/signin.html")

@login_required
def acccount(request):
    return render(
        request,
        "users/account.html",{
            "user": request.user
        })

def signout(request):
    logout(request)
    return redirect("home")