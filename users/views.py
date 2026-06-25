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

    if request.method == "POST":
        user = request.user

        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.username = request.POST.get("username")
        user.email = request.POST.get("email")

        user.save()

        return redirect("account")
    
    return render(request, "users/account.html")



def signout(request):
    logout(request)
    return redirect("home")