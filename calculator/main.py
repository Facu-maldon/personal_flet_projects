import flet as ft
    
async def main(page: ft.Page):

    global total_operation
    total_operation = ""

    global current_number
    current_number = 0

    global numbers
    numbers = []

    global operations
    operations = []

    def do_operation():
        global total_operation
        global result
        result = eval(total_operation)
        total_operation = f"{result}"
        print(result)

        screen.value = result
        page.update()
        
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
    page.window_height = 500
    page.window_width = 400
    page.title = "Calculator"
    page.window_center()

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
                operations.append("+")
                total_operation = f"{total_operation}{value}"

            elif value == "-":
                operations.append("-")
                total_operation = f"{total_operation}{value}"

            elif value == "*":
                operations.append("*")
                total_operation = f"{total_operation}{value}"

            elif value == "/":
                operations.append("/")
                total_operation = f"{total_operation}{value}"

            elif value == "=":
                do_operation()
            
            else:
                total_operation = ""
        
        screen.value = total_operation
        page.update()

    keys = ft.GridView(
        runs_count=4,
        height=page.window.height*60/100,
        width=page.window_width,
        child_aspect_ratio=1.8,
    )
    
    screen = ft.TextField(read_only=True,
                          value=total_operation,
                          height=page.window.height*20/100,
                          width=page.window_width,
                          color=ft.colors.WHITE)
    
    mainColumn = ft.Column(
        [
            screen,
            ft.Container(keys, alignment=ft.alignment.bottom_center),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        height=page.window_height,
        width=page.window_width
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
