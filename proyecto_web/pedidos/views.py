from django.shortcuts import render, redirect
from carro.carro import Carro
from pedidos.models import Pedido, LineaPedido
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.core.mail import send_mail

@login_required(login_url="/Autenticacion/loguear")

def procesar_pedido(request):
    pedido = Pedido.objects.create(user=request.user)
    carro = Carro(request)
    lineas_pedidos = list()
    for key,value in carro.carro.items():
        lineas_pedidos.append(LineaPedido(
            producto_id = key, 
            cantidad = value["cantidad"],
            user = request.user,
            pedido = pedido,
        ))

    LineaPedido.objects.bulk_create(lineas_pedidos)

    enviar_email(
        pedido = pedido,
        lineas_pedidos = lineas_pedidos,
        nombre_usuario = request.user.username,
        email_usuario = request.user.email,
    )

    messages.success(request, "datos almacenados correctamente, el pedido esta hecho")
    return redirect("../tienda")

def enviar_email(**kwargs):
    asunto = "Muchas Gracias por el Pedido"
    mensaje = render_to_string("emails/pedido.html", {
        "pedido": kwargs.get("pedido"),
        "lineas_pedidos": kwargs.get("lineas_pedidos"),
        "nombre_usuario": kwargs.get("nombre_usuario"),
    })
    mensaje_texto = strip_tags(mensaje)
    from_email = "jeiprogrammers@gmail.com"
    #to = kwargs.get("email_usuario")
    to = "ceferinoberriojeferson@gmail.com"

    send_mail(asunto, mensaje_texto, from_email, [to], html_message=mensaje)
    
