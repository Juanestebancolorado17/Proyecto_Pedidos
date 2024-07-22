from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from carro.carro import Carro
from servicios.models import Servicios
from info.models import Informacion
from proyecto_web.forms import FormularioContacto
from django.core.paginator import Paginator
# Create your views here.


def home(request):
    carro = Carro(request)
    return render(request, 'home.html')

def servicios(request):
    listado = Servicios.objects.all()
    paginator = Paginator(listado, 1)
    pagina = request.GET.get("page") or 1
    lista = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, lista.paginator.num_pages + 1)
    return render(request, 'servicios.html', {'servicios': lista, 'paginas': paginas, 'pagina_actual': pagina_actual })


# def tienda(request):
#     return render(request, 'tienda.html')

# def blog(request):
#     return render(request, 'blog.html')

def contacto(request):
    i = Informacion.objects.all()
    return render(request, 'contacto.html', {'informacion':i})



# fragmento de codigo para el envio de correos para contacto
#--------------------------------------------------------------
# def enviar(request):
#     if request.method == "POST":
#         nombre = request.POST["nombre"]
#         subject = request.POST["asunto"]
#         asunto = request.POST["asunto"]
#         message = "El usuario: " + nombre + "\nEnvío mensaje: " + request.POST["mensaje"] + "\ncon el correo: " + request.POST["correo"]
#         email_from = settings.EMAIL_HOST_USER
#         recipient_list = ["jeiprogrammers@gmail.com"]
#         send_mail(subject, message, email_from, recipient_list)
#         return HttpResponse("<h1>Gracias por enviar</h1>")
#     return render(request, "contacto.html")
#--------------------------------------------------------------

def formulario(request):
    formulario = FormularioContacto() # creo variable formulario que contendra todos los valores del formulario creado en forms.py
    if request.method== "POST": # evaluo si el metodo es post verificable en el html de formulario.html
        formulario=FormularioContacto(data=request.POST) #captura los datos del formulario que son: email, contenido, y nombre
        if formulario .is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")
            email = EmailMessage("App Refugio Jei Programmers",
                                 "El usuario {} con email {} envió el siguiente asunto \n\n{}".format(nombre,email,contenido),
                                 "",["jeiprogrammers@gmail.com"], reply_to=[email])
            try:
                email.send()
                return redirect("/formulario/?valido")
            except:
                return redirect("/formulario/?invalido")
    return render(request, "formulario.html", {"miformulario": formulario})



