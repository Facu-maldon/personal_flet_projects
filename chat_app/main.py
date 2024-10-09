import flet as ft
import pymysql as sql

def main(page: ft.Page):

    def test(e):
        pass

    user_chats = [{"id": 1, "username": "Facu", "last_message": "test"}]

    class Chat(ft.ListTile):

        global id_count
        id_count = 0

        def __init__(self, username, last_message):
            super().__init__()
            global id_count

            self.leading = ft.Text(username)
            self.subtitle = ft.Text(last_message)
            self.id = id_count
            id_count += 1

        def build(self):
            self.bgcolor = ft.colors.YELLOW
            self.hover_color = ft.colors.BLACK
            self.bgcolor_activated = ft.colors.GREEN
            self.on_click = test
            self.visual_density = ft.VisualDensity.ADAPTIVE_PLATFORM_DENSITY
            self.leading = ft.Image(src="assets/icon.png")
            return self
        
        class Message(ft.Text()):
            pass

            
    def adapt(e):
        chatsRow.height = e.height
        chatsRow.width = e.width*30/100

        mainChat.height = e.height
        mainChat.width = e.width*70/100

        mainColumn.height = e.height
        mainColumn.width = e.width

        page.update()


    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.on_resized = adapt
    
    chatsRow = ft.ResponsiveRow(height=page.window.height, width=page.window.width*30/100)

    for chat in user_chats:
        chatsRow.controls.append(Chat(chat.get("username"), chat.get("last_message"))) 

    mainChat = ft.ResponsiveRow([ft.Container(bgcolor=ft.colors.RED)], height=page.window.height, width=page.window.width*63/100)

    mainColumn = ft.Column(controls=[chatsRow, ft.VerticalDivider(leading_indent=10, trailing_indent=10), mainChat],
                           wrap=True,
                           expand=True,
                           horizontal_alignment=ft.CrossAxisAlignment.START,
                           alignment=ft.MainAxisAlignment.START)

    page.add(mainColumn)

ft.app(main)
