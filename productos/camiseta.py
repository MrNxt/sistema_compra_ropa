# productos/camiseta.py
from prenda import Prenda

class Camiseta(Prenda):
    def __init__(self, descripcion, costo, talla):
        super().__init__(descripcion, costo)
        self.talla = talla

    def aplicar_oferta(self):
        return self.costo * 0.92