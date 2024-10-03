import pandas as pd

to_read = "C:/Users/Usuario2/Desktop/Pasantias/test_csv.xlsx"

file = pd.read_excel(to_read)

file = file.head(len(file))

datos = [i for i in file]

longitudes = [4, 10, 3, 6, 4, 9, 13, 30, 2, 8]

if len(datos) != len(longitudes):
    print("Error en la carga de datos")

for i in range(0, len(file)):
    
    contador_longitudes = 0
    linea = ""
    for dato in datos:

        dato = file[dato][i]
        long = len(str(dato))
        faltantes = longitudes[contador_longitudes]-long

        try:
            dato = int(dato)

            if len(str(dato)) < longitudes[contador_longitudes]:
                dato = int(f"{dato}{"0"*faltantes}")

        except ValueError:
            dato = str(dato)
            if len(dato) < longitudes[contador_longitudes]:
                dato = f"{dato}{" "*faltantes}"

        linea = f"{linea}{dato}"
        print(dato, len(str(dato)))
        contador_longitudes += 1
        

    linea = f"{linea}\n"
    print(linea, len(linea), linea[0])

