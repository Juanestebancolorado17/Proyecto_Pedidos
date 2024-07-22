class Carro:  # Clase que representa un carrito de compras.
    def __init__(self, request):  # Constructor de la clase, recibe un objeto 'request'.
        self.request = request  # Establece el atributo 'request' de la instancia como el objeto recibido.
        self.session = request.session  # Establece el atributo 'session' de la instancia como el atributo 'session' del objeto 'request'.
        carro = self.session.get("carro")  # Intenta obtener el carrito de la sesión.
        if not carro:  # Si el carrito no existe en la sesión o está vacío:
            carro = self.session["carro"] = {}  # Crea un nuevo carrito vacío en la sesión.
        #else:  # Si el carrito existe en la sesión y no está vacío: 
        self.carro = carro  # Establece el atributo 'carro' de la instancia como el carrito existente.
    
    def agregar(self,producto):# funcion agregar instancia self y parametro producto
        if (str(producto.id)not in self.carro.keys()):# si el producto.id como string
            self.carro[producto.id]={
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad": 1,
                "imagen": producto.imagen.url}
        else:
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value["cantidad"]=value["cantidad"]+1
                    value["precio"]=float(value["precio"])+producto.precio
                    break
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified=True

    def eliminar(self, producto):
        producto.id=str(producto.id)

        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()

    def restar(self, producto):
        for key,value in self.carro.items():
            if key == str(producto.id):
                value ["cantidad"]=value["cantidad"]-1
                value ["precio"]=float(value["precio"])-producto.precio
                if value ["cantidad"]<1:
                    self.eliminar(producto)
                    break
        self.guardar_carro()

    def limpiar(self):
        self.session["carro"]={}
        self.session.modified=True