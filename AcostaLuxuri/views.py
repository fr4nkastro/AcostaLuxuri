import _imp
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from lib.userLib  import LibUser
from lib.accesorio import Accesorio
from lib.libAccesorio import LibAccesorio

def index(request): 
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")

def accesorio(request):
    return render(request,"create.html")  

def create_accesorio(request):
    return render(request,"create.html")

def insert_accesorio(request):
    codigo = request.POST['codigo']
    nombre = request.POST['nombre']
    descripcion = request.POST['descripcion']
    precio = request.POST['precio']
    libAccesorio = LibAccesorio()
    resp = libAccesorio.create(codigo,nombre,descripcion,precio)
    if(resp):
        return redirect("/home")
    else:
        return redirect("/accesorio/crear")

def edit_accesorio(request):
    codigo = request.POST['codigo']
    libAccesorio = LibAccesorio()
    accesorio = libAccesorio.get_accesorios_by_codigo(codigo)
    return render(request,"edit.html",{'accesorio':accesorio})

def update_accesorio(request):
    codigo = request.POST['codigo']
    nombre = request.POST['nombre']
    descripcion = request.POST['descripcion']
    precio = request.POST['precio']
    libAccesorio = LibAccesorio()
    resp = libAccesorio.edit(codigo,nombre,descripcion,precio)
    if(resp):
        return redirect("/home")
    else:
        return redirect("/accesorio/edit?codigo="+codigo)
    
def remove_accesorio(request):
    codigo = request.GET['codigo']
    libAccesorio = LibAccesorio()
    accesorio = libAccesorio.get_accesorios_by_codigo(codigo)
    return render(request,"remove.html",{'accesorio':accesorio})

def delete_accesorio(request):
    codigo = request.POST['codigo']
    libAccesorio = LibAccesorio()
    resp = libAccesorio.eliminar(codigo)
    if(resp):
        return redirect("/home")
    else:
        return redirect("/accesorio/remove?codigo="+codigo)

def iniciar(request):
    libUser = LibUser()
    email = request.POST['email']
    password = request.POST['password']
    resp = libUser.login(email, password)
    if(resp):

        return redirect("/home")
    else: 
        return redirect("/login")
    
def home(request):
    libAccesorio = LibAccesorio()
    lista = libAccesorio.get_accesorios()

    return render(request,"home.html",{"lista":lista})

#def mostrar_accesorios(request):
    # Leer el archivo JSON
    #file = open('data/productos.json', 'r')
    #data = json.load(file)
    
    # Pasar los datos a la plantilla
    #return render(request, 'index.html', {'accesorios': data['accesorios,']})