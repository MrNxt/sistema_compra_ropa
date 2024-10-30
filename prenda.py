# prenda.py
class Prenda:
    def __init__(self, descripcion, costo):
        self.descripcion = descripcion
        self.costo = costo

    def aplicar_oferta(self):
        return self.costo

    def __str__(self):
        return f"{self.descripcion} - ${self.costo:.2f}"
