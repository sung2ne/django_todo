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
    
# 프로필, /common/profile/
def common_profile(request):
    if request.method == "POST":
        email = request.POST["email"]
        last_name = request.POST["last_name"]
        request.user.email = email
        request.user.last_name = last_name
        request.user.save()
        return redirect("common:profile")
    else:
        context = {}
        return render(request, "common/profile.html", context)
    
# 비밀번호, /common/password/
def common_password(request):
    if request.method == "POST":
        password = request.POST["password"]
        request.user.set_password(password)
        request.user.save()
        return redirect("common:profile")