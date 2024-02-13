class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f"Carro: {self.marca} {self.modelo}"

class Barco:
    def __init__(self, nombre, longitud):
        self.nombre = nombre
        self.longitud = longitud

    def __str__(self):
        return f"Barco: {self.nombre}, Longitud: {self.longitud}"

class Avion:
    def __init__(self, fabricante, capacidad):
        self.fabricante = fabricante
        self.capacidad = capacidad

    def __str__(self):
        return f"Avion: {self.fabricante}, Capacidad: {self.capacidad}"

def registrar_carro():
    marca = input("Ingrese la marca del carro: ")
    modelo = input("Ingrese el modelo del carro: ")
    return Carro(marca, modelo)

def registrar_barco():
    nombre = input("Ingrese el nombre del barco: ")
    longitud = float(input("Ingrese la longitud del barco en metros: "))
    return Barco(nombre, longitud)

def registrar_avion():
    fabricante = input("Ingrese el fabricante del avión: ")
    capacidad = int(input("Ingrese la capacidad de pasajeros del avión: "))
    return Avion(fabricante, capacidad)


def mostrar_vehiculos_registrados(vehiculos):
    if not vehiculos:
        print("No hay vehículos registrados.")
    else:
        print("Vehículos registrados:")
        for vehiculo in vehiculos:
            print(vehiculo)


def main():
    vehiculos = []
    while True:
        print("\n¿Qué desea hacer?")
        print("1. Registrar un carro")
        print("2. Registrar un barco")
        print("3. Registrar un avión")
        print("4. Mostrar vehículos registrados")
        print("5. Salir")

        opcion = input("Ingrese el número de opción: ")

        if opcion == "1":
            vehiculo = registrar_carro()
            vehiculos.append(vehiculo)
            print("Carro registrado con éxito!")
        elif opcion == "2":
            vehiculo = registrar_barco()
            vehiculos.append(vehiculo)
            print("Barco registrado con éxito!")
        elif opcion == "3":
            vehiculo = registrar_avion()
            vehiculos.append(vehiculo)
            print("Avión registrado con éxito!")
        elif opcion == "4":
            mostrar_vehiculos_registrados(vehiculos)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()

