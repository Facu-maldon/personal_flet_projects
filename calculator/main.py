import flet as ft
    
async def main(page: ft.Page):

    def buttons(text, bgndcolor, textcolor, btnheight, btnwidth):
        return ft.TextButton(text=text,
                height=btnheight,
                width=btnwidth,
                style=ft.ButtonStyle(bgcolor=bgndcolor, color=textcolor))
    
    page.bgcolor = ft.colors.BLACK
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.window_height = 600
    page.window_width = 400
    page.title = "Calculator"
    page.window_center()

    def keyPress(value):
        number = f"{number}{value}"

    number = ""

    keys = ft.GridView( runs_count=4,
                        height=page.window_height,
                        width=page.window_width,
                        child_aspect_ratio=1.8,
                        bottom=0)
    
    screen = ft.TextField(read_only=True, value=number)
    
    mainStack = ft.Stack([ft.Container(bgcolor=ft.colors.AMBER), keys, screen],
                        height=page.window_height,
                        width=page.window_width,
                        alignment=ft.alignment.center,
                        )
    
    keys.controls.append(buttons("1",ft.colors.WHITE, ft.colors.BLACK, keys.height/7, keys.width/4.5))
    keys.controls.append(buttons("2",ft.colors.WHITE, ft.colors.BLACK, keys.height/7, keys.width/4.5))
    keys.controls.append(buttons("3",ft.colors.WHITE, ft.colors.BLACK, keys.height/7, keys.width/4.5))
    keys.controls.append(buttons("+",ft.colors.WHITE, ft.colors.BLACK, keys.height/7, keys.width/4.5))

    keys.controls.append(buttons("4",ft.colors.WHITE, ft.colors.BLACK, keys.height/7, keys.width/4.5))
    keys.controls.append(buttons("5",ft.colors.WHITE, ft.colors.BLACK, keys.height/7, keys.width/4.5))
    keys.controls.append(buttons("6",ft.colors.WHITE, ft.colors.BLACK, keys.height/7, keys.width/4.5))
    keys.controls.append(buttons("-",ft.colors.WHITE, ft.colors.BLACK, keys.height/7, keys.width/4.5))

    keys.controls.append(buttons("7",ft.colors.WHITE, ft.colors.BLACK, keys.height/7, keys.width/4.5))
    keys.controls.append(buttons("8",ft.colors.WHITE, ft.colors.BLACK, keys.height/7, keys.width/4.5))
    keys.controls.append(buttons("9",ft.colors.WHITE, ft.colors.BLACK, keys.height/7, keys.width/4.5))
    keys.controls.append(buttons("*",ft.colors.WHITE, ft.colors.BLACK, keys.height/7, keys.width/4.5))

    keys.controls.append(buttons("AC",ft.colors.WHITE, ft.colors.BLACK, keys.height/7, keys.width/4.5))
    keys.controls.append(buttons("0",ft.colors.WHITE, ft.colors.BLACK, keys.height/7, keys.width/4.5))
    keys.controls.append(buttons("=",ft.colors.WHITE, ft.colors.BLACK, keys.height/7, keys.width/4.5))
    keys.controls.append(buttons("/",ft.colors.WHITE, ft.colors.BLACK, keys.height/7, keys.width/4.5))
    

    page.add(mainStack)


ft.app(main)
