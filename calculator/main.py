import flet as ft
    
async def main(page: ft.Page):

    global total_operation
    total_operation = ""
        
    def buttons(value, bgndcolor, textcolor, btnheight, btnwidth):

        return ft.TextButton(text=value,
                height=btnheight,
                width=btnwidth,
                style=ft.ButtonStyle(bgcolor=bgndcolor, color=textcolor),
                data=value,
                on_click=keyPress)

    page.bgcolor = ft.colors.BLACK
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.window.height = 500
    page.window.width = 400
    page.title = "Calculator"
    page.window.center()

    def keyPress(a):

        value = a.control.data
        try:
            int(value)
            global total_operation
            total_operation = f"{total_operation}{value}"
        except:
            if total_operation[-1] == "+" or total_operation[-1] == "-" or total_operation[-1] == "*" or total_operation[-1] == "/":
                return 0
            
            if value == "+":
                total_operation = f"{total_operation}{value}"

            elif value == "-":
                total_operation = f"{total_operation}{value}"

            elif value == "*":
                total_operation = f"{total_operation}{value}"

            elif value == "/":
                total_operation = f"{total_operation}{value}"

            elif value == "=":
                total_operation = f"{eval(total_operation)}"
                page.update()
            
            else:
                total_operation = ""
        
        screen.value = total_operation
        page.update()

    keys = ft.GridView(
        runs_count=4,
        height=page.window.height*60/100,
        width=page.window.width,
        child_aspect_ratio=1.8,
    )
    
    screen = ft.TextField(read_only=True,
                          value=total_operation,
                          height=page.window.height*20/100,
                          width=page.window.width,
                          color=ft.colors.WHITE)
    
    mainColumn = ft.Column(
        [screen, ft.Container(keys, alignment=ft.alignment.bottom_center)],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        height=page.window.height,
        width=page.window.width
    )
    
    keys.controls.append(buttons("1",ft.colors.WHITE, ft.colors.BLACK, keys.height/7, keys.width/4.5))
    keys.controls.append(buttons("2",ft.colors.WHITE, ft.colors.BLACK, keys.height/7, keys.width/4.5))
    keys.controls.append(buttons("3",ft.colors.WHITE, ft.colors.BLACK, keys.height/7, keys.width/4.5))
    keys.controls.append(buttons("+",ft.colors.AMBER_ACCENT_700, ft.colors.BLACK, keys.height/7, keys.width/4.5))

    keys.controls.append(buttons("4",ft.colors.WHITE, ft.colors.BLACK, keys.height/7, keys.width/4.5))
    keys.controls.append(buttons("5",ft.colors.WHITE, ft.colors.BLACK, keys.height/7, keys.width/4.5))
    keys.controls.append(buttons("6",ft.colors.WHITE, ft.colors.BLACK, keys.height/7, keys.width/4.5))
    keys.controls.append(buttons("-",ft.colors.AMBER_ACCENT_700, ft.colors.BLACK, keys.height/7, keys.width/4.5))

    keys.controls.append(buttons("7",ft.colors.WHITE, ft.colors.BLACK, keys.height/7, keys.width/4.5))
    keys.controls.append(buttons("8",ft.colors.WHITE, ft.colors.BLACK, keys.height/7, keys.width/4.5))
    keys.controls.append(buttons("9",ft.colors.WHITE, ft.colors.BLACK, keys.height/7, keys.width/4.5))
    keys.controls.append(buttons("*",ft.colors.AMBER_ACCENT_700, ft.colors.BLACK, keys.height/7, keys.width/4.5))

    keys.controls.append(buttons("AC",ft.colors.RED_400, ft.colors.BLACK, keys.height/7, keys.width/4.5))
    keys.controls.append(buttons("0",ft.colors.WHITE, ft.colors.BLACK, keys.height/7, keys.width/4.5))
    keys.controls.append(buttons("=",ft.colors.BLUE_ACCENT_700, ft.colors.BLACK, keys.height/7, keys.width/4.5))
    keys.controls.append(buttons("/",ft.colors.AMBER_ACCENT_700, ft.colors.BLACK, keys.height/7, keys.width/4.5))
    

    page.add(mainColumn)


ft.app(main)
