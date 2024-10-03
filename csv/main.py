import flet as ft
from screeninfo import get_monitors

def main(page: ft.Page):

    def mostrarArchivo(e: ft.FilePickerResultEvent):
        print(nombreArchivo)
        nombreArchivo.helper_text = e.files
        rutaArchivo.helper_text = e.path
        page.update()


    monitores = get_monitors()

    page.window.width = monitores[0].width/5
    page.window.height = monitores[0].height/2

    page.title = "Formateador Excel a TXT"

    selector = ft.FilePicker(on_result=mostrarArchivo)

    page.overlay.append(selector)

    global nombreArchivo

    global rutaArchivo

    nombreArchivo = ft.TextField(label="Nombre del archivo", disabled=True)

    rutaArchivo = ft.TextField(label="Ruta del archivo", disabled=True)

    columna = ft.ResponsiveRow([ft.ElevatedButton(on_click=lambda _: selector.pick_files(), text="Elegir archivo"),
                                nombreArchivo, rutaArchivo],
                                height=page.window.height, width=page.window.width)



    page.add(columna)

ft.app(main)
