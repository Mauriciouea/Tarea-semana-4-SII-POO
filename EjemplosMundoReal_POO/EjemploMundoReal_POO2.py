class TiendaPrimeraNecesidad:
    def __init__(self):
        self.inventario = []
        self.ventas_totales = 0
        self.compras_totales = 0
    
    def agregar_articulo(self, nombre, color, tamaño, precio, cantidad):
        """Agrega un nuevo artículo al inventario"""
        nuevo_articulo = {
            'nombre': nombre,
            'color': color,
            'tamaño': tamaño,
            'precio': precio,
            'cantidad': cantidad,
            'vendidos': 0
        }
        self.inventario.append(nuevo_articulo)
        print(f"➕ Artículo agregado: {nombre} ({cantidad} unidades)")
    
    def vender(self, nombre_articulo, cantidad=1):
        """Vende una cantidad específica de un artículo"""
        for articulo in self.inventario:
            if articulo['nombre'] == nombre_articulo:
                if articulo['cantidad'] >= cantidad:
                    articulo['cantidad'] -= cantidad
                    articulo['vendidos'] += cantidad
                    self.ventas_totales += articulo['precio'] * cantidad
                    print(f"💰 Vendido: {cantidad} {nombre_articulo} por ${articulo['precio'] * cantidad}")
                    return
                else:
                    print(f"⚠️ No hay suficiente stock de {nombre_articulo} (Solo {articulo['cantidad']} disponibles)")
                    return
        print(f"❌ Artículo no encontrado: {nombre_articulo}")
    
    def comprar(self, nombre_articulo, cantidad=1):
        """Reabastece el inventario de un artículo"""
        for articulo in self.inventario:
            if articulo['nombre'] == nombre_articulo:
                articulo['cantidad'] += cantidad
                self.compras_totales += articulo['precio'] * cantidad * 0.7  # Costo para la tienda (70% del precio)
                print(f"🛒 Comprado: {cantidad} {nombre_articulo} - Stock actual: {articulo['cantidad']}")
                return
        print(f"❌ Artículo no encontrado: {nombre_articulo}")
    
    def mostrar_inventario(self):
        """Muestra el estado actual del inventario"""
        print("\n📦 INVENTARIO ACTUAL:")
        print("{:<20} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
            "Artículo", "Color", "Tamaño", "Precio", "Stock", "Vendidos"))
        print("-"*70)
        for articulo in self.inventario:
            print("{:<20} {:<10} {:<10} ${:<9} {:<10} {:<10}".format(
                articulo['nombre'],
                articulo['color'],
                articulo['tamaño'],
                articulo['precio'],
                articulo['cantidad'],
                articulo['vendidos']))
        
        print(f"\n📊 RESUMEN FINANCIERO:")
        print(f"Ventas totales: ${self.ventas_totales}")
        print(f"Compras totales: ${self.compras_totales:.2f}")
        print(f"Ganancias estimadas: ${(self.ventas_totales - self.compras_totales):.2f}")


# Ejemplo de uso
mi_tienda = TiendaPrimeraNecesidad()

# Agregar artículos básicos
mi_tienda.agregar_articulo("Arroz", "blanco", "1kg", 2.50, 100)
mi_tienda.agregar_articulo("Frijoles", "negros", "500g", 3.00, 80)
mi_tienda.agregar_articulo("Aceite", "transparente", "1L", 4.20, 50)
mi_tienda.agregar_articulo("Azúcar", "blanca", "2kg", 2.80, 60)

# Operaciones de compra/venta
mi_tienda.vender("Arroz", 5)
mi_tienda.vender("Frijoles", 3)
mi_tienda.vender("Leche", 2)  # Artículo no existente
mi_tienda.comprar("Arroz", 20)
mi_tienda.vender("Aceite", 10)
mi_tienda.comprar("Azúcar", 15)

# Mostrar estado final
mi_tienda.mostrar_inventario()

