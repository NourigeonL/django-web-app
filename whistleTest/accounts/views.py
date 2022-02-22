from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from whistleTest.settings import DEBUG
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions


def index(request):
    return HttpResponse("Accounts index")


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/patients')
    else:
        form = AuthenticationForm(request)
    context = {
        "form": form
    }
    return render(request, "accounts/login.html", context)


def logout_view(request):
    print("logout")
    if request.method == "POST":
        logout(request)
        return redirect('/login/')
    return render(request, "accounts/logout.html", {})


# @api_view(["GET"])
# @permission_classes([permissions.IsAuthenticated])
# def User_logout(request):

#     request.user.auth_token.delete()

#     logout(request)

#     return Response('User Logged out successfully')
