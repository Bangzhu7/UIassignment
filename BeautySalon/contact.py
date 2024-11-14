import flet as ft
import webbrowser

def ContactPage():
    return ft.Container(
        content=ft.Column(
            [
                # Contact Header
                ft.Text(
                    'Contact', 
                    size=60,
                    weight=ft.FontWeight.W_500,
                    font_family="Futura",
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Text(
                    'I\'m a paragraph. Click here to add your own text and edit me. It\'s easy. Just click "Edit Text" or double click me to add your own content and make changes to the font. I\'m a great place for you to tell a story and let your users know a little more about you.',
                    size=16, 
                    font_family="Futura",
                    color=ft.colors.GREY_800,
                    text_align=ft.TextAlign.CENTER,
                    width=600
                ),
                # Static Map Image with Clickable Link
                ft.Container(
                    content=ft.GestureDetector(
                        on_tap=lambda e: webbrowser.open("https://www.google.com/maps/place/Beauty+Salon"),
                        content=ft.Image(
                            src="https://maps.googleapis.com/maps/api/staticmap?center=Beauty+Salon&zoom=15&size=800x400&key=AIzaSyALUF_ugEtkXn5tXT0cYrf0eqOQ8UubyRgY",
                            width=800,
                            height=400,
                            fit=ft.ImageFit.COVER,
                        )
                    ),
                    margin=ft.margin.only(top=20),
                    border_radius=10
                ),
                # Form Fields
                ft.Row(
                    [
                        ft.TextField(label="First Name *", width=350),
                        ft.TextField(label="Last Name *", width=350),
                    ],
                    spacing=20,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [
                        ft.TextField(label="Email *", width=350),
                        ft.TextField(label="Phone", width=350),
                    ],
                    spacing=20,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.TextField(
                    label="Leave us a message...",
                    multiline=True,
                    min_lines=4,
                    width=720
                ),
                # Submit Button without EdgeInsets
                ft.Container(
                    content=ft.ElevatedButton(
                        text="Submit",
                        on_click=lambda e: print("Form submitted!"),
                        style=ft.ButtonStyle(
                            bgcolor=ft.colors.BLACK,
                            color=ft.colors.WHITE,
                            padding=20  # Setting padding without EdgeInsets
                        )
                    ),
                    alignment=ft.alignment.center,
                    margin=ft.margin.only(top=20)
                ),
            ],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll="auto"  # Enables scrolling only when necessary

            ),
        
        padding=ft.padding.only(top=40),
        alignment=ft.alignment.center,
        width=1000,  # Set width if needed for layout consistency
        height=600   # Set height to limit the viewable area and activate scrolling
    )