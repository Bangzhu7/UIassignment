import flet as ft

def AboutPage():
    return ft.Container(
        content=ft.Column(
            [
                ft.Text('About', 
                    size=60,
                    weight=ft.FontWeight.W_500,
                    font_family="Futura",
                    text_align=ft.TextAlign.CENTER
                        ),
                ft.Text(
                    'I\'m a paragraph. Click here to add your own text and edit me. It \'s easy. Just click "Edit Text" or double click me to add your own content and make changes to the font. I\'m a great place for you to tell a story and let your users know a little more about you.',
                    size=16, 
                    font_family="Futura",
                    color=ft.colors.GREY_800,
                    text_align=ft.TextAlign.CENTER,
                    width=600
                ),
                ft.Container(
                    content=ft.Image(
                        src="D:\Pictures\elegant_cat.jfif",  # This uses a random placeholder image
                        width=800,
                        height=400,
                        fit=ft.ImageFit.COVER,
                    ),
                    margin=ft.margin.only(top=20),
                    border_radius=10  # Optional: adds rounded corners to the image
                )
            ],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER

        ),
        
        padding=ft.padding.only(top=40),
        alignment=ft.alignment.center
    )