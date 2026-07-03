from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from users.models import User


def signin(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("home")

        return render(
            request,
            "users/signin.html",
            {"error": " Zły login lub hasło"}
        )
    return render(request, "users/signin.html")


@login_required
def acccount(request):

    if request.method == "POST":
        user = request.user

        user.first_name = request.POST.get("first_name") or user.first_name
        user.last_name = request.POST.get("last_name") or user.last_name
        user.username = request.POST.get("username") or user.username
        user.email = request.POST.get("email") or user.email
        if "avatar" in request.FILES:
            user.avatar = request.FILES["avatar"]
        user.modified_at = datetime.datetime.now()

        user.save()

        return redirect("account")

    return render(request, "users/account.html")


def signout(request):
    logout(request)
    return redirect("home")


def signup(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password,
            avatar="users/default_avatar.jpg"
        )

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)

        return redirect("home")

    return render(request, "users/signup.html")
