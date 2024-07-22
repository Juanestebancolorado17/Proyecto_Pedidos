#elimine el admin del proyecto junto con el path
from django.urls import path
from proyectowebapp import views
from django.conf import settings
from django.conf.urls.static import static # cargar el static
 
urlpatterns = [
    path('', views.home, name='home' ),
    path('servicios/', views.servicios, name='servicios'),
    # path('tienda/', views.tienda, name='tienda' ),
    # path('blog/', views.blog, name='blog'),
    path('contacto/', views.contacto, name='contacto'),
    # path('enviar/', views.enviar),
    path('formulario/', views.formulario, name='formulario'),

]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT) # generar las imagenes

