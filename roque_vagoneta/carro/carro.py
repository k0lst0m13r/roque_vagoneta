

class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")
        if not carro:
            carro = self.session['carro'] = {}
        #else:
        self.carro = carro


    def agregar(self, articulo):
        if (str(articulo.id) not in self.carro.keys()):
            self.carro[articulo.id] = {
                "articulo_id": articulo.id,
                "nombre": articulo.nombre,
                "cantidad": 1,
                "precio": str(articulo.precio),
            }
        else:
            for key, value in self.carro.items():
                if key == str(articulo.id):
                    value["cantidad"] = value["cantidad"] + 1
                    break
        self.guardar_carro()


    def eliminar(self, articulo):
        articulo.id = str(articulo.id)
        if articulo.id in self.carro:
            del self.carro[articulo.id]
            self.guardar_carro()


    def sacar(self, articulo):
        for key, value in self.carro.items():
            if key == str(articulo.id):
                value["cantidad"] = value["cantidad"] - 1
                if value["cantidad"] < 1:
                    self.eliminar(articulo)
                break
        self.guardar_carro()


    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True

    def vaciar_carro(self):
        self.session['carro'] = {}
        self.session.modified = True
