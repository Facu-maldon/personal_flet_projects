import flet as ft

class botonesCalculo():
    def __init__(self, bgcolor):
        self.bgcolor = ft.colors(bgcolor=bgcolor)
    
def main(page: ft.Page):

    page.bgcolor = ft.colors.BLACK
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    teclas = ft.ResponsiveRow(alignment=ft.MainAxisAlignment.CENTER,
                              vertical_alignment=ft.CrossAxisAlignment.CENTER,
                              height=page.height,
                              width=page.width)

    teclas.controls.append(
        ft.Row([
            ft.TextButton(text="1",
                        height=teclas.height/8,
                        width=teclas.width/10,
                        style=ft.ButtonStyle(bgcolor=ft.colors.WHITE)),
            ft.TextButton(text="4",
                        height=teclas.height/8,
                        width=teclas.width/10,
                        style=ft.ButtonStyle(bgcolor=ft.colors.WHITE)),
            ft.TextButton(text="7",
                        height=teclas.height/8,
                        width=teclas.width/10,
                        style=ft.ButtonStyle(bgcolor=ft.colors.WHITE)),
            ft.TextButton(text="AC",
                        height=teclas.height/8,
                        width=teclas.width/10,
                        style=ft.ButtonStyle(bgcolor=ft.colors.WHITE)),
    ]))

    teclas.controls.append(
        ft.Row([
            ft.TextButton(text="2",
                        height=teclas.height/8,
                        width=teclas.width/10,
                        style=ft.ButtonStyle(bgcolor=ft.colors.WHITE)),
            ft.TextButton(text="5",
                        height=teclas.height/8,
                        width=teclas.width/10,
                        style=ft.ButtonStyle(bgcolor=ft.colors.WHITE)),
            ft.TextButton(text="8",
                        height=teclas.height/8,
                        width=teclas.width/10,
                        style=ft.ButtonStyle(bgcolor=ft.colors.WHITE)),
            ft.TextButton(text="0",
                        height=teclas.height/8,
                        width=teclas.width/10,
                        style=ft.ButtonStyle(bgcolor=ft.colors.WHITE)),
    ]))

    teclas.controls.append(
        ft.Row([
            ft.TextButton(text="3",
                        height=teclas.height/8,
                        width=teclas.width/10,
                        style=ft.ButtonStyle(bgcolor=ft.colors.WHITE)),
            ft.TextButton(text="6",
                        height=teclas.height/8,
                        width=teclas.width/10,
                        style=ft.ButtonStyle(bgcolor=ft.colors.WHITE)),
            ft.TextButton(text="9",
                        height=teclas.height/8,
                        width=teclas.width/10,
                        style=ft.ButtonStyle(bgcolor=ft.colors.WHITE)),
            ft.TextButton(text="=",
                        height=teclas.height/8,
                        width=teclas.width/10,
                        style=ft.ButtonStyle(bgcolor=ft.colors.WHITE)),
    ]))

    teclas.controls.append(
        ft.Row([
            ft.TextButton(text="+",
                        height=teclas.height/8,
                        width=teclas.width/10,
                        style=ft.ButtonStyle(bgcolor=ft.colors.WHITE)),
            ft.TextButton(text="-",
                        height=teclas.height/8,
                        width=teclas.width/10,
                        style=ft.ButtonStyle(bgcolor=ft.colors.WHITE)),
            ft.TextButton(text="*",
                        height=teclas.height/8,
                        width=teclas.width/10,
                        style=ft.ButtonStyle(bgcolor=ft.colors.WHITE)),
            ft.TextButton(text="/",
                        height=teclas.height/8,
                        width=teclas.width/10,
                        style=ft.ButtonStyle(bgcolor=ft.colors.WHITE)),
    ]))

    page.add(teclas)


ft.app(main)
