import pandas as pd


def formatearExcelATxt(archivoOrigen):
    dataFrame = pd.read_excel(archivoOrigen)
    dataFrame = dataFrame.head(len(dataFrame))

    datos = [i for i in dataFrame]

    longitudes = [4, 10, 3, 6, 4, 9, 13, 30, 2, 8]

    if len(datos) != len(longitudes):
        print("Error en la carga de datos")
        return 2

    for i in range(0, len(dataFrame)):
        
        contador_longitudes = 0
        linea = ""
        if len(dataFrame["Numero de documento"][i]) != 8:
            print(f"Número de documento de la columna {i} incorrecto(escribirlo sin puntos y revisar error en la escritura)")
            return 1
        
        for dato in datos:

            dato = dataFrame[dato][i]
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
            contador_longitudes += 1
            

        linea = f"{linea}\n"


