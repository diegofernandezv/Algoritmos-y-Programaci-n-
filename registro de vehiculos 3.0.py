class Seller:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.vehicles_sold = []

    def __str__(self):
        return f"Concesionario: {self.nombre}, Ubicación: {self.ubicacion}"

    def add_vehicle(self, vehicle):
        self.vehicles_sold.append(vehicle)

    def display_vehicles_sold(self):
        print(f"Vehículos vendidos por {self} :")
        for vehicle in self.vehicles_sold:
            print(vehicle)

class Vehicle:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"Vehículo: {self.nombre}"

class Carro(Vehicle):
    def __init__(self, nombre, seller, marca, modelo):
        super().__init__(nombre)
        self.seller = seller
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f"Carro: {self.marca} {self.modelo}, Vehículo: {self.nombre}"

class Barco(Vehicle):
    def __init__(self, nombre, seller, longitud):
        super().__init__(nombre)
        self.seller = seller
        self.longitud = longitud

    def __str__(self):
        return f"Barco: {self.nombre}, Longitud: {self.longitud}, Vehículo: {self.nombre}"

class Avion(Vehicle):
    def __init__(self, nombre, seller, fabricante, capacidad):
        super().__init__(nombre)
        self.seller = seller
        self.fabricante = fabricante
        self.capacidad = capacidad

    def __str__(self):
        return f"Avión: {self.fabricante}, Capacidad: {self.capacidad}, Vehículo: {self.nombre}"

def main():
    seller1 = Seller("Concesionario Vehicle Dealership C.A", "Ciudad Caracas")
    seller2 = Seller("Concesionario Toyota & Company ", "Ciudad Valencia")
 
    while True:
        print("\nSelecciona una opción:")
        print("1. Registrar un carro")
        print("2. Registrar un barco")
        print("3. Registrar un avión")
        print("4. Ver vehículos vendidos")
        print("5. Salir")

        option = int(input("Opción: "))

        if option == 1:
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            carro = Carro(f"Carro {marca} {modelo}", seller1, marca, modelo)
            vendedor = int(input("Vendido por (1 para Vehicle Dealership C.A, 2 para Concesionario Toyota & Company): "))
            if vendedor == 1:
                seller1.add_vehicle(carro)
            elif vendedor == 2:
                seller2.add_vehicle(carro)
            else:
                print("Opción inválida")
        elif option == 2:
            nombre = input("Nombre: ")
            longitud = float(input("Longitud: "))
            barco = Barco(nombre, seller1, longitud)
            vendedor = int(input("Vendido por (1 para Vehicle Dealership C.A, 2 para Concesionario Toyota & Company): "))
            if vendedor == 1:
                seller1.add_vehicle(barco)
            elif vendedor == 2:
                seller2.add_vehicle(barco)
            else:
                print("Opción inválida")
        elif option == 3:
            nombre = input("Nombre: ")
            fabricante = input("Fabricante: ")
            capacidad = int(input("Capacidad: "))
            avion = Avion(nombre, seller1, fabricante, capacidad)
            vendedor = int(input("Vendido por (1 para Vehicle Dealership C.A, 2 para Concesionario Toyota & Company): "))
            if vendedor == 1:
                seller1.add_vehicle(avion)
            elif vendedor == 2:
                seller2.add_vehicle(avion)
            else:
                print("Opción inválida")
        elif option == 4:
            print("Vehículos vendidos por Vehicle Dealership C.A:")
            seller1.display_vehicles_sold()
            print("Vehículos vendidos por Concesionario Toyota & Company:")
            seller2.display_vehicles_sold()
        elif option == 5:
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()

"""
PSEUDOCODIGO

Clase Vendedor:
    Función Inicializar(nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.vehiculos_vendidos = []

    Función Agregar_vehiculo(vehiculo):
        Agregar vehiculo a self.vehiculos_vendidos

Clase Vehiculo:
    Función Inicializar(nombre):
        self.nombre = nombre

Función Principal():
    Mientras Verdadero:
        Mostrar_Menu()
        opcion = Obtener_Opcion()
        
        Si opcion es igual a 1:
            Registrar_Vehiculo("Carro")
        Sino, Si opcion es igual a 2:
            Registrar_Vehiculo("Barco")
        Sino, Si opcion es igual a 3:
            Registrar_Vehiculo("Avión")
        Sino, Si opcion es igual a 4:
            Mostrar_Vehiculos_Vendidos()
        Sino, Si opcion es igual a 5:
            Romper
        Sino:
            Imprimir "Opción inválida"

Función Mostrar_Menu():
    Imprimir "Selecciona una opción:"
    Imprimir "1. Registrar un carro"
    Imprimir "2. Registrar un barco"
    Imprimir "3. Registrar un avión"
    Imprimir "4. Ver vehículos vendidos"
    Imprimir "5. Salir"

Función Obtener_Opcion():
    Devolver Convertir_a_entero(Entrada de usuario("Opción: "))

Función Registrar_Vehiculo(tipo):
    nombre = Entrada de usuario("Nombre: ")
    Si tipo es igual a "Carro":
        Marca = Entrada de usuario("Marca: ")
        Modelo = Entrada de usuario("Modelo: ")
        Vehiculo = Nuevo Carro("Carro " + Marca + " " + Modelo)
    Sino, Si tipo es igual a "Barco":
        Longitud = Convertir_a_flotante(Entrada de usuario("Longitud: "))
        Vehiculo = Nuevo Barco(nombre, Longitud)
    Sino:
        Fabricante = Entrada de usuario("Fabricante: ")
        Capacidad = Convertir_a_entero(Entrada de usuario("Capacidad: "))
        Vehiculo = Nuevo Avion(nombre, Fabricante, Capacidad)

    Vendedor = Seleccionar_Vendedor()
    Vendedor.Agregar_vehiculo(Vehiculo)

Función Seleccionar_Vendedor():
    Imprimir "Selecciona el concesionario (A o B): "
    Vendedor = Obtener_Opcion()
    Si Vendedor es igual a A:
        Devolver Nuevo Vendedor("Concesionario A")
    Sino:
        Devolver Nuevo Vendedor("Concesionario B")

Función Mostrar_Vehiculos_Vendidos():
    Para cada vendedor en Lista_de_vendedores:
        Imprimir "Vehículos vendidos por " + vendedor.nombre
        Para cada vehiculo en vendedor.vehiculos_vendidos:
            Imprimir vehiculo.nombre

Si __nombre__ es igual a "__principal__":
    Principal()


"""