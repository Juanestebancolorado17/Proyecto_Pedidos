
from django.contrib import admin
from django.urls import path,include #include para incluir
from blog import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('proyectowebapp.urls')),
    path('blog/', include('blog.urls')),
    path('autenticacion/', include('autenticacion.urls')),
    path('table/', views.table, name='table'),
    path('', include('tienda.urls')),
    path('carro/', include('carro.urls')), #Redireccionar el carrito.
    path('pedidos/', include('pedidos.urls')),
]