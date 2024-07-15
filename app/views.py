from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from .models import Suscripciones
from .forms import SuscripcionesForm
from .forms import PersonaForm
from .forms import LoginForm
from django.contrib.auth.hashers import make_password
from .models import Persona
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import CarroItem
from django.shortcuts import get_object_or_404, redirect
from .models import CarroItem, Revista
from django.shortcuts import render
from .models import CarroItem
from django.shortcuts import get_object_or_404, redirect
from .models import CarroItem, Revista
def admin_view(request):
    return render(request, 'admin_view.html')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, 
                                    username = cd['username'],
                                    password = cd['password']) # None
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Usuario autenticado')
                else:
                    return HttpResponse('el usuario no esta activo')
            else:
                return HttpResponse('la informacion no es correcta')
    else:
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})
      

def home(request):
    suscripcion = Suscripciones.objects.all()
    return render(request, 'app/index.html',{'suscripciones': suscripcion})

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

def register(request):
    formulario = PersonaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('home')
    return render(request, 'app/register.html',{'formulario':formulario})

def revista(request):
    suscripcion = Suscripciones.objects.all()
    print(suscripcion)
    return render(request, 'revistas/index.html', {'suscripciones': suscripcion})

def crear(request):
    formulario = SuscripcionesForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('revista')
    return render(request, 'revistas/crear.html',{'formulario': formulario})

def editar(request, id):
    suscripciones = Suscripciones.objects.get(id=id)
    formulario = SuscripcionesForm(request.POST or None, request.FILES or None, instance=suscripciones)
    if formulario.is_valid() and request.POST :
        formulario.save()
        return redirect('revista')
    return render(request, 'revistas/editar.html',{'formulario': formulario})

def eliminar(request,id):
    suscripciones = Suscripciones.objects.get(id=id)
    suscripciones.delete() 
    return redirect('revista')



def agregar_al_carro(request, revista_id):
    revista = get_object_or_404(Revista, pk=revista_id)
    carro_usuario, creado = CarroItem.objects.get_or_create(
        revista=revista,
        usuario=request.user
    )
    if not creado:
        carro_usuario.cantidad += 1
        carro_usuario.save()
    return redirect('vista_del_carro') 


def vista_del_carro(request):
    carro_items = CarroItem.objects.filter(usuario=request.user)
    total = sum(item.revista.precio * item.cantidad for item in carro_items)
    return render(request, 'app/vista_del_carro.html', {'carro_items': carro_items, 'total': total})

