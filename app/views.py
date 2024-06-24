from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

def admin_view(request):
    return render(request, 'admin_view.html')  

def home(request):
    return render(request, 'app/index.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return JsonResponse({"error": "Invalid username or password"}, status=400)
        else:
            return JsonResponse({"error": "Invalid form"}, status=400)
    else:
        form = AuthenticationForm()
    return render(request, 'app/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'app/register.html', {'form': form})

def noticia2(request):
    return render(request, 'app/noticia2.html')

def noticia3(request):
    return render(request, 'app/noticia3.html')

def noticia4(request):
    return render(request, 'app/noticia4.html')

def carrete(request):
    return render(request, 'app/carrete.html')

def servicios(request):
    return render(request, 'app/servicios.html')

def revistas(request):
    return render(request, 'app/revistas.html')

def revista(request):
    return render(request, 'revistas/index.html')