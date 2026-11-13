import csv
datos = [
    [ "nombre" , "costo" , "cantidad"],
    ["manzana", 0.5, 10],
    ["banana", 0.3, 15],
]
with open("datos.csv", "w", newline="") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(datos)
    