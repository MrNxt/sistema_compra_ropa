# tienda.py
class TiendaDeRopa:
    def __init__(self, nombre_tienda):
        self.nombre_tienda = nombre_tienda
        self.inventario = []

    def agregar_prenda(self, prenda):
        self.inventario.append(prenda)

    def listar_prendas(self):
        print(f"Inventario de {self.nombre_tienda}:")
        for indice, prenda in enumerate(self.inventario, 1):
            print(f"{indice}. {prenda}")

    def realizar_compra(self, seleccion):
        if 1 <= seleccion <= len(self.inventario):
            prenda = self.inventario[seleccion - 1]
            precio_final = prenda.aplicar_oferta()
            print(f"Compra realizada: {prenda.descripcion} - Precio con descuento: ${precio_final:.2f}")
        else:
            print("Selección no válida.")
