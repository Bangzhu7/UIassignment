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
                    font_family="Verdana",
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Text(
                    "Get in Touch with Us",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    font_family="Verdana",
                    color=ft.colors.GREY_800,
                ),
                ft.Text(
                    "We’d love to hear from you! Whether you have questions about our services, want to make an appointment, or need expert advice on beauty care, we’re here to help.",
                    size=16,
                    weight=ft.FontWeight.NORMAL,
                    font_family="Verdana",
                    color=ft.colors.GREY_800,
                ),
                ft.Text(
                    "Our Contact Details",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    font_family="Verdana",
                    color=ft.colors.GREY_800,
                ),
                ft.Row(
                    [
                        ft.Icon(ft.icons.LOCATION_ON, color=ft.colors.PINK, size=20),
                        ft.Text(
                            "Address: Microkatu 1",
                            size=16,
                        ),
                    ],
                ),
                ft.Row(
                    [
                        ft.Icon(ft.icons.PHONE, color=ft.colors.RED, size=20),
                        ft.Text(
                            "Phone: 041234566",
                            size=16,
                        ),
                    ],
                ),
                ft.Row(
                    [
                        ft.Icon(ft.icons.EMAIL, color=ft.colors.BLUE, size=20),
                        ft.Text(
                            "Email: catbeauty@gmail.com",
                            size=16,
                        ),
                    ],
                ),
                 ft.Text(
                    "Business Hours",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    font_family="Verdana",
                    color=ft.colors.GREY_800,
                ),
                ft.Text(
                    """Monday – Friday: 9:00 AM – 7:00 PM
                    Saturday: 10:00 AM – 6:00 PM
                    Sunday: Closed""",
                    size=16,
                    weight=ft.FontWeight.NORMAL,
                    font_family="Verdana",
                    color=ft.colors.GREY_800,
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
                    margin=ft.margin.only(top=20, bottom=40)
                ),
            ],
           scroll=ft.ScrollMode.AUTO,  # Enable scrolling for the column
            spacing=20,  # Add consistent spacing between elements
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Center align all content
            expand=True,  # Allow the column to expand to full height
        ),
        expand=True,  # Allow the container to expand to full height
        padding=ft.padding.symmetric(horizontal=20),  # Add horizontal padding
    )