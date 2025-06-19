class GranjaAgricola:
    def __init__(self):
        self.inventario_animales = []
        self.inventario_cultivos = []
        self.balance = 0  # Dinero disponible en la granja

    def agregar_animal(self, nombre, color, tamaño, precio_venta, precio_compra):
        animal = {
            'nombre': nombre,
            'color': color,
            'tamaño': tamaño,
            'precio_venta': precio_venta,
            'precio_compra': precio_compra,
            'cantidad': 0
        }
        self.inventario_animales.append(animal)

    def agregar_cultivo(self, nombre, color, tamaño, precio_venta, precio_compra):
        cultivo = {
            'nombre': nombre,
            'color': color,
            'tamaño': tamaño,
            'precio_venta': precio_venta,
            'precio_compra': precio_compra,
            'cantidad': 0
        }
        self.inventario_cultivos.append(cultivo)

    def comprar(self, tipo, nombre, cantidad):
        if tipo == 'animal':
            for animal in self.inventario_animales:
                if animal['nombre'] == nombre:
                    costo_total = animal['precio_compra'] * cantidad
                    if self.balance >= costo_total:
                        animal['cantidad'] += cantidad
                        self.balance -= costo_total
                        print(f"Comprados {cantidad} {nombre}(s). Costo: ${costo_total}")
                    else:
                        print("Fondos insuficientes")
                    return
        elif tipo == 'cultivo':
            for cultivo in self.inventario_cultivos:
                if cultivo['nombre'] == nombre:
                    costo_total = cultivo['precio_compra'] * cantidad
                    if self.balance >= costo_total:
                        cultivo['cantidad'] += cantidad
                        self.balance -= costo_total
                        print(f"Comprados {cantidad} {nombre}(s). Costo: ${costo_total}")
                    else:
                        print("Fondos insuficientes")
                    return
        print(f"{nombre} no encontrado en inventario de {tipo}s")

    def vender(self, tipo, nombre, cantidad):
        if tipo == 'animal':
            for animal in self.inventario_animales:
                if animal['nombre'] == nombre:
                    if animal['cantidad'] >= cantidad:
                        ingreso_total = animal['precio_venta'] * cantidad
                        animal['cantidad'] -= cantidad
                        self.balance += ingreso_total
                        print(f"Vendidos {cantidad} {nombre}(s). Ingreso: ${ingreso_total}")
                    else:
                        print(f"No hay suficiente cantidad de {nombre} (Disponibles: {animal['cantidad']})")
                    return
        elif tipo == 'cultivo':
            for cultivo in self.inventario_cultivos:
                if cultivo['nombre'] == nombre:
                    if cultivo['cantidad'] >= cantidad:
                        ingreso_total = cultivo['precio_venta'] * cantidad
                        cultivo['cantidad'] -= cantidad
                        self.balance += ingreso_total
                        print(f"Vendidos {cantidad} {nombre}(s). Ingreso: ${ingreso_total}")
                    else:
                        print(f"No hay suficiente cantidad de {nombre} (Disponibles: {cultivo['cantidad']})")
                    return
        print(f"{nombre} no encontrado en inventario de {tipo}s")

    def mostrar_inventario(self):
        print("\n=== INVENTARIO DE ANIMALES ===")
        for animal in self.inventario_animales:
            print(f"{animal['nombre']}: {animal['cantidad']} disponibles - Color: {animal['color']} - Tamaño: {animal['tamaño']}")

        print("\n=== INVENTARIO DE CULTIVOS ===")
        for cultivo in self.inventario_cultivos:
            print(f"{cultivo['nombre']}: {cultivo['cantidad']} disponibles - Color: {cultivo['color']} - Tamaño: {cultivo['tamaño']}")

        print(f"\nBalance actual: ${self.balance}")

# Ejemplo de uso
if __name__ == "__main__":
    mi_granja = GranjaAgricola()
    mi_granja.balance = 10000  # Fondos iniciales
    
    # Agregar productos disponibles
    mi_granja.agregar_animal("Vaca", "Blanco y negro", "Grande", 1200, 800)
    mi_granja.agregar_animal("Gallo", "Rojo", "Pequeño", 50, 30)
    mi_granja.agregar_cultivo("Maíz", "Amarillo", "Mediano", 5, 3)
    mi_granja.agregar_cultivo("Tomate", "Rojo", "Pequeño", 8, 5)
    
    # Operaciones
    mi_granja.comprar('animal', 'Vaca', 2)
    mi_granja.comprar('cultivo', 'Maíz', 100)
    mi_granja.vender('animal', 'Vaca', 1)
    mi_granja.vender('cultivo', 'Maíz', 50)
    
    # Mostrar estado final
    mi_granja.mostrar_inventario()