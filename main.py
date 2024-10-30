from tienda import TiendaDeRopa
from productos.camiseta import Camiseta
from productos.jean import Jean
from prenda import Prenda

if __name__ == "__main__":
    tienda = TiendaDeRopa("Moda Actual")
    tienda.agregar_prenda(Camiseta("Camiseta Verde", 35.00, "M"))
    tienda.agregar_prenda(Jean("Jean Azul", 60.00, "L"))

    tienda.listar_prendas()
    eleccion = int(input("Seleccione el número de la prenda que desea comprar: "))
    tienda.realizar_compra(eleccion)
