from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

# 로그아웃, /common/logout/
def common_logout(request):
    logout(request)
    return redirect("todo:index")

# 로그인, /common/login/
def common_login(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        
        if username and password:
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect("todo:index")
            else:
                # Authentication failed
                context = {"error": "잘못된 사용자명 또는 비밀번호입니다."}
                return render(request, "common/login.html", context)
        else:
            # Missing username or password
            context = {"error": "사용자명과 비밀번호를 모두 입력해주세요."}
            return render(request, "common/login.html", context)
    else:
        context = {}
        return render(request, "common/login.html", context)
    
# 프로필, /common/profile/
@login_required
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
@login_required
def common_password(request):
    if request.method == "POST":
        password = request.POST.get("password", "")
        
        if password and len(password) >= 8:  # Basic password validation
            request.user.set_password(password)
            request.user.save()
            
            # Re-authenticate user after password change
            from django.contrib.auth import update_session_auth_hash
            update_session_auth_hash(request, request.user)
            
            return redirect("common:profile")
        else:
            context = {"error": "비밀번호는 최소 8자 이상이어야 합니다."}
            return render(request, "common/password.html", context)
    else:
        context = {}
        return render(request, "common/password.html", context)