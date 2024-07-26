from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect, render

# 로그아웃, /common/logout/
def common_logout(request):
    logout(request)
    return redirect("todo:index")

# 로그인, /common/login/
def common_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
        return redirect("todo:index")
    else:
        context = {}
        return render(request, "common/login.html", context)