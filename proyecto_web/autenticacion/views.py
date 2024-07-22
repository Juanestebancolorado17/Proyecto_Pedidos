from django.shortcuts import render, redirect
from django.views.generic import View #para cargar las vistas genericas que me ofrece django
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm #Creación del usuario en formulario y hacer la validación
from django.contrib.auth import login, logout, authenticate # Permite hacer el logueo de la tabla autenticación 
from django.contrib import messages # Permite cargar la libreria de mensajes de django para errores




# def autenticacion(request):
#     return render(request, 'registro/registro.html

class VRegistro(View):# inicializacion de una clase vista para el registro
    def get(self, request):# metodo para get 
        form = UserCreationForm # variable que permite la creacion del formulario
        return render(request, 'registro/registro.html', {'form': form})# retorna el archivo renderizado de registro.html y el formulario con sus campos
    
    def post(self, request): 
        form = UserCreationForm(request.POST)  #para la creacion del formulario y peticion del post y que capture                    # pass para que no salga error en caso de no tener nada aun 
        if form.is_valid():
            usuario = form.save() # crear un usuario y guardar 
            login(request, usuario) # 
            messages.success(request, "Usuario registrado")
            return redirect('home')
        else:
            for msg in form.error_messages: # errores posibles en el formulario
                messages.error(request,form.error_messages[msg])
        return render(request, "registro/registro.html",{"form" : form})
    


def cerrar_sesion(request):
    logout(request)
    return redirect('home')


def loguear(request): #Crearemos la vista con la autenticación
    if request.method=='POST': # Verificar si el metodo es de post
        form = AuthenticationForm(request, data=request.POST) # Pase la petición y que por medio de data captura los datos que están en el formulario del logueo
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get('username')
            contrasena = form.cleaned_data.get('password')
            usuario = authenticate(username=nombre_usuario, password=contrasena) # Estamos cargando en usuario la autenticación de los dos campos
            if usuario is not None: #Si el usuario no está
                login(request, usuario)
                return redirect('home')
            else:
                messages.error(request, 'USUARIO NO LOGUEADO')
        else:
            messages.error(request, 'INFORMACION INCORRECTA PENDEJO!!!')
    form = AuthenticationForm()
    return render(request, 'login/login.html', {'form':form})
