from django.shortcuts import render, redirect

def dashboard_home(request):
    if 'user_id' not in request.session:
        return redirect("users:login")

    email = request.session.get("email")
    return render(request, "dashboard.html", {"email": email})
