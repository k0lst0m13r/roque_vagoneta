

class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")
        if not carro:
            carro = self.session['carro'] = {}
        else:
            self.carro = carro

    def agregar_articulo(self, articulo):
        if (str(articulo.id) not in self.carro.keys()):
            self.carro[articulo.id] = {
                "articulo_id": articulo_id,
                "nombre": nombre,
                "cantidad": 1,
                "precio": precio,
            }
        else:
            for key, value in self.carro.items():
                if key == str(articulo.id):
                    value["cantidad"] = value["cantidad"] + 1
                    break
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True

    def eliminar(self, articulo):
        articulo.id = str(articulo.id)
        if articulo.id is in self.carro:
            del self.carro[articulo.id]
            self.guardar_carro()

    def sacar_articulo(self, articulo):
        for key, value in self.carro.items():
            if key == str(articulo.id):
                value["cantidad"] = value["cantidad"] - 1
                if value["cantidad"] < 1:
                    self.eliminar(articulo)
                break
        self.guardar_carro()


    def vaciar_carro():
        self.session['carro'] = {}
        self.session.modified = True
