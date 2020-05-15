import os

def sumar_fn(valor_1, valor_2):
    return int(valor_1) + int(valor_2)

print("----------------------------")
print("Menu:") 
print("1-sumar")
print("")
print("9-salir")
print("")
print("----------------------------")
opcion = input("seleccione la opción deseada: ")
print("----------------------------")
if opcion == "1" :
    valor_1 = input("ingrese el primer valor: ")
    valor_2 = input("ingrese el segundo valor: ")
    print("Resultado = " + str(sumar_fn(valor_1, valor_2)))
