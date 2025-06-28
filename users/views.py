from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import CustomUser

from documents.models import Download
import json



def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        role = request.POST['role']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Les mots de passe ne correspondent pas.")
            return redirect('register')

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Ce nom d'utilisateur est déjà utilisé.")
            return redirect('register')

        # Créer l'utilisateur
        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password1,
            role=role  # Ici tu définis le rôle directement
        )
 
        return redirect('user_login')

    return render(request, "users/register.html")


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # 🔁 Redirection selon le rôle
            
            if user.role == "student":
                return redirect("student_dashboard")
             
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")

    return render(request, "users/login.html")

def user_logout(request):
    logout(request)
    messages.success(request, "Vous avez été déconnecté avec succès.")
    return redirect('login')



# views pour les differents dashboard
@login_required
def student_dashboard(request):
     
    cours_count = Download.objects.filter(user=request.user, document__doc_type='course').count()
    devoir_count = Download.objects.filter(user=request.user, document__doc_type='assignment').count()
    examen_count = Download.objects.filter(user=request.user, document__doc_type='exam').count()


# les datas selon les rubriques
    chart_data = {
        'labels': ['Cours', 'Devoirs', 'Examens'],
        'data': [cours_count, devoir_count, examen_count],
    }

    return render(request, "users/student_dashboard.html", context= {
        "cours_count": cours_count,
        "devoir_count": devoir_count,
        "examen_count": examen_count,
        'chart_data': json.dumps(chart_data),
    }
    )
 

 