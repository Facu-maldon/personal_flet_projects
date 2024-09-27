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
    page.window.height = 800
    page.window.width = 700
    page.title = "Calculator"

    mainStack = ft.Stack([ft.Container(bgcolor=ft.colors.AMBER)],
                         height=page.window.height,
                         width=page.window.width,
                         alignment=ft.alignment.center)

    keys = ft.ResponsiveRow(height=mainStack.height*60/100,
                            width=mainStack.width,
                            bottom=0,
                            left=0)
    
    mainStack.controls.append(keys)
    
    keys.controls.append(
        ft.Row([
            buttons("1",ft.colors.WHITE, ft.colors.BLACK, keys.height/7, keys.width/4.5),
            buttons("2",ft.colors.WHITE, ft.colors.BLACK, keys.height/7, keys.width/4.5),
            buttons("3",ft.colors.WHITE, ft.colors.BLACK, keys.height/7, keys.width/4.5),
            buttons("+",ft.colors.WHITE, ft.colors.BLACK, keys.height/7, keys.width/4.5),
                ],
            width=keys.width,
            alignment=ft.MainAxisAlignment.CENTER
        ))

    keys.controls.append(
        ft.Row([
            buttons("4",ft.colors.WHITE, ft.colors.BLACK, keys.height/7, keys.width/4.5),
            buttons("5",ft.colors.WHITE, ft.colors.BLACK, keys.height/7, keys.width/4.5),
            buttons("6",ft.colors.WHITE, ft.colors.BLACK, keys.height/7, keys.width/4.5),
            buttons("-",ft.colors.WHITE, ft.colors.BLACK, keys.height/7, keys.width/4.5),
                ],
                )
        )

    keys.controls.append(
        ft.Row([
            buttons("7",ft.colors.WHITE, ft.colors.BLACK, keys.height/7, keys.width/4.5),
            buttons("8",ft.colors.WHITE, ft.colors.BLACK, keys.height/7, keys.width/4.5),
            buttons("9",ft.colors.WHITE, ft.colors.BLACK, keys.height/7, keys.width/4.5),
            buttons("*",ft.colors.WHITE, ft.colors.BLACK, keys.height/7, keys.width/4.5),
                ], 
            ))

    keys.controls.append(
        ft.Row([
            buttons("AC",ft.colors.WHITE, ft.colors.BLACK, keys.height/7, keys.width/4.5),
            buttons("0",ft.colors.WHITE, ft.colors.BLACK, keys.height/7, keys.width/4.5),
            buttons("=",ft.colors.WHITE, ft.colors.BLACK, keys.height/7, keys.width/4.5),
            buttons("/",ft.colors.WHITE, ft.colors.BLACK, keys.height/7, keys.width/4.5),
                ]))
    

    page.add(mainStack)


ft.app(main)
