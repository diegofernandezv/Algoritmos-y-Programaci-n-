year = int(input("Dime un año entre 1900 y 2199: "))

if year % 4 != 0:
    print("No es bisiesto")
elif year % 4 == 0 and year % 100 != 0:
    print("Es bisiesto")
elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
    print("No es bisiesto")
elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print("Es bisiesto")

bisiestos_number = 0
for i in range(1900, year + 1):
    if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
        bisiestos_number += 1

print(f"El número de años bisiestos entre 1900 y {year} es: {bisiestos_number}")







