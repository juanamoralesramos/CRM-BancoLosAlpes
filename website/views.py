from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Cliente
from .forms import CrearClienteForm
from .serializers import ClienteSerializer
from rest_framework import generics

# Create your views here.
def home(request):
    #todos los clientes
    clientes =Cliente.objects.all()
    
    
    #Mirar si la persona hizo log in
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        #Autenticar a la persona
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('home')
        else:
            messages.success(request, "Hubo un error, intente de nuevo!")
            return redirect('home')
    else:
        return render(request, 'home.html', {'clientes': clientes})

""" def login_user(request):
    pass """

def logout_user(request):
    logout(request)
    messages.success(request, "Salió de la sesión...")
    return redirect('home')

def customer_cliente(request, pk):
    #solo el que este logueado lo puede hacer
    if request.user.is_authenticated:
        #mirar al cliente por si id GET
        customer_cliente = Cliente.objects.get(id=pk)
        return render(request, 'cliente.html', {'customer_cliente': customer_cliente})
    else:
        messages.success(request, "Debe iniciar sesión para visualizar la información.")
        return redirect('home')

""" def crear_cliente(request):
    form = CrearClienteForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                crear_cliente = form.save()
                messages.success(request, "Cliente Creado...")
                return redirect('home')
        return render(request, 'crear_cliente.html', {'form': form})
    else: 
        messages.success(request, "Debe haber iniciado sesión...")
        return redirect('home') """
def crear_cliente(request):
    form = CrearClienteForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "Cliente Creado...")
                return redirect('home')
            else:
                print(form.errors)  # Esto imprimirá los errores del formulario en la consola
        return render(request, 'crear_cliente.html', {'form': form})
    else: 
        messages.success(request, "Debe haber iniciado sesión...")
        return redirect('home')

class ClienteDetailView(generics.RetrieveAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    lookup_field = 'pk'  # Asume que estás buscando clientes por ID