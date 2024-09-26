import flet as ft
    
async def main(page: ft.Page):

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
            ft.TextButton(text="1",
                        height=keys.height/7,
                        width=keys.width/4.5,
                        style=ft.ButtonStyle(bgcolor=ft.colors.WHITE)),
            ft.TextButton(text="2",
                        height=keys.height/7,
                        width=keys.width/4.5,
                        style=ft.ButtonStyle(bgcolor=ft.colors.WHITE)),
            ft.TextButton(text="3",
                        height=keys.height/7,
                        width=keys.width/4.5,
                        style=ft.ButtonStyle(bgcolor=ft.colors.WHITE)),
            ft.TextButton(text="+",
                        height=keys.height/7,
                        width=keys.width/4.5,
                        style=ft.ButtonStyle(bgcolor=ft.colors.WHITE)),
                ],

    ))

    keys.controls.append(
        ft.Row([
            ft.TextButton(text="4",
                        height=keys.height/7,
                        width=keys.width/4.5,
                        style=ft.ButtonStyle(bgcolor=ft.colors.WHITE)),
            ft.TextButton(text="5",
                        height=keys.height/7,
                        width=keys.width/4.5,
                        style=ft.ButtonStyle(bgcolor=ft.colors.WHITE)),
            ft.TextButton(text="6",
                        height=keys.height/7,
                        width=keys.width/4.5,
                        style=ft.ButtonStyle(bgcolor=ft.colors.WHITE)),
            ft.TextButton(text="-",
                        height=keys.height/7,
                        width=keys.width/4.5,
                        style=ft.ButtonStyle(bgcolor=ft.colors.WHITE)),
                ],
                )
        )

    keys.controls.append(
        ft.Row([
            ft.TextButton(text="7",
                        height=keys.height/7,
                        width=keys.width/4.5,
                        style=ft.ButtonStyle(bgcolor=ft.colors.WHITE)),
            ft.TextButton(text="8",
                        height=keys.height/7,
                        width=keys.width/4.5,
                        style=ft.ButtonStyle(bgcolor=ft.colors.WHITE)),
            ft.TextButton(text="9",
                        height=keys.height/7,
                        width=keys.width/4.5,
                        style=ft.ButtonStyle(bgcolor=ft.colors.WHITE)),
            ft.TextButton(text="*",
                        height=keys.height/7,
                        width=keys.width/4.5,
                        style=ft.ButtonStyle(bgcolor=ft.colors.WHITE)),
                ], 
            ))

    keys.controls.append(
        ft.Row([
            ft.TextButton(text="AC",
                        height=keys.height/7,
                        width=keys.width/4.5,
                        style=ft.ButtonStyle(bgcolor=ft.colors.WHITE)),
            ft.TextButton(text="0",
                        height=keys.height/7,
                        width=keys.width/4.5,
                        style=ft.ButtonStyle(bgcolor=ft.colors.WHITE)),
            ft.TextButton(text="=",
                        height=keys.height/7,
                        width=keys.width/4.5,
                        style=ft.ButtonStyle(bgcolor=ft.colors.WHITE)),
            ft.TextButton(text="/",
                        height=keys.height/7,
                        width=keys.width/4.5,
                        style=ft.ButtonStyle(bgcolor=ft.colors.WHITE)),
                ],
                alignment=ft.MainAxisAlignment.CENTER))
    

    page.add(mainStack)


ft.app(main)
