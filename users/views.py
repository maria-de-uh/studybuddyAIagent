from django.shortcuts import render, redirect
from db.mongo import users_collection

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        user = users_collection.find_one({"email": email, "password": password})
        
        if user:
            request.session['user_id'] = str(user['_id'])
            request.session['email'] = user['email']
            return redirect("dashboard:home")
        else:
            return render(request, "login.html", {"error": "Invalid credentials."})
    
    return render(request, "login.html")
