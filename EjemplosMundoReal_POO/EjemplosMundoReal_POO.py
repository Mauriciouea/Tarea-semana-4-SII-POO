class Bicicleta:
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
        self.velocidad = 0  # Atributo adicional para controlar la velocidad

    def frenar(self, cantidad):
        """Reduce la velocidad de la bicicleta."""
        if self.velocidad - cantidad >= 0:
            self.velocidad -= cantidad
            print(f"Frenando... Velocidad actual: {self.velocidad} km/h")
        else:
            self.velocidad = 0
            print("¡La bicicleta se ha detenido completamente!")

    def acelerar(self, cantidad):
        """Aumenta la velocidad de la bicicleta."""
        self.velocidad += cantidad
        print(f"Acelerando... Velocidad actual: {self.velocidad} km/h")

    def __str__(self):
        return f"Bicicleta {self.marca} de color {self.color} (Velocidad: {self.velocidad} km/h)"


# Ejemplo de uso
mi_bici = Bicicleta("Giant", "rojo")
print(mi_bici)  # Muestra los detalles iniciales

mi_bici.acelerar(15)  # Acelera en 15 km/h
mi_bici.acelerar(10)  # Acelera otros 10 km/h
mi_bici.frenar(5)     # Frena 5 km/h
mi_bici.frenar(30)    # Intenta frenar más de lo necesario
