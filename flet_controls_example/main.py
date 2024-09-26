import flet as ft
import time

#Main control aka Page
def main(page: ft.Page):
    #Text control
    t1 = ft.Text(value="Hello, world!", color="green")

    #Appending controls
    page.controls.append(t1)

    page.update()

    '''-----------------------------------------------------'''

    #Updating controls on execution

    t2 = ft.Text()

    for i in range(3):
        t2.value = f"Step {i}"

        page.add(t2) # it's a shortcut for page.controls.append(t) and then page.update()
        time.sleep(1)

    '''-----------------------------------------------------'''

    #Container controls: used to place onther controls inside them
    row1 = ft.Row(controls=[
        ft.Text("A"),
        ft.Text("B"),
        ft.Text("C")
    ])

    page.add(row1)
    
    row2 = ft.Row(controls=[
        ft.TextField(label="Your name"),
        ft.ElevatedButton(text="Say my name!")
    ])
    page.add(row2)

ft.app(main)
