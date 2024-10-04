import flet as ft
import pandas as pd
from reader import formatearExcelATxt
from screeninfo import get_monitors

def main(page: ft.Page):
    def mostrarArchivo(e: ft.FilePickerResultEvent):
        archivo = e.files[0]

        columna.controls.pop()
        columna.controls.pop()

        columna.controls.append(ft.Text(f"Nombre del archivo:\n {archivo.name}"))
        columna.controls.append(ft.Text(f"Ruta del archivo:\n {archivo.path.replace("\\", "/")}"))

        botonConvertir.data = archivo.path.replace("\\", "/")
        botonConvertir.on_click = formatearExcelATxt

        page.update()
        
    pantallas = get_monitors()

    page.window.width = pantallas[0].width/5
    page.window.height = pantallas[0].height/2

    page.title = "Formateador Excel a TXT"

    selector = ft.FilePicker(on_result=mostrarArchivo)

    page.overlay.append(selector)

    columna = ft.ResponsiveRow([ft.ElevatedButton(
                                    on_click=lambda _: selector.pick_files(file_type=ft.FilePickerFileType.CUSTOM,
                                    allowed_extensions = ["xls", "xlsx"],
                                    allow_multiple = False), 
                                    text="Elegir archivo"),
                                ft.Text("Archivo no seleccionado"),
                                ft.Text()],
                                height=page.window.height*75/100, width=page.window.width)
    
    global botonConvertir
    botonConvertir = ft.ElevatedButton(text="Convertir")

    columnaBoton = ft.ResponsiveRow([botonConvertir],height=page.window.height*25/100, width=page.window.width)

    page.controls.append(columna)

    page.add(columnaBoton)

ft.app(main)
