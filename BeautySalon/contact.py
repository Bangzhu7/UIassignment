import flet as ft
import webbrowser

def ContactPage(page: ft.Page):

    firstname_error = ft.Text("", color=ft.colors.RED_400)
    lastname_error = ft.Text("", color=ft.colors.RED_400)
    email_error = ft.Text("", color=ft.colors.RED_400)

    firstname=ft.TextField(label="First Name *", width=350)
    lastname=ft.TextField(label="Last Name *", width=350)
    email=ft.TextField(label="Email *", width=350)
    phone = ft.TextField(label="Phone", width=350)
    message = ft.TextField(
        label="Leave us a message...",
        multiline=True,
        min_lines=4,
        width=720
    )

    def show_submit_dialog(e):
        # Create and show the dialog
        submit_dialog = ft.AlertDialog(
            title=ft.Text("Form Submitted"),
            content=ft.Text("Thank you for your message! We'll get back to you soon."),
            actions=[
                ft.TextButton("Close", on_click=lambda e: page.close_dialog())
            ]
        )
        page.dialog = submit_dialog
        submit_dialog.open = True
        page.update()

    def handle_submit(e):
        is_valid = True
        firstname_error.value = ""
        lastname_error.value = ""
        email_error.value = ""
        
        if not firstname.value:
            firstname_error.value = "First name cannot be blank!"
            is_valid = False
        
        if not lastname.value:
            lastname_error.value = "Last name cannot be blank!"
            is_valid = False

        if not email.value:
            email_error.value = "Email cannot be blank!"
            is_valid = False
            
        if is_valid:
            show_submit_dialog(e),
        
        page.update()
       

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
                    width=700,
                ),
                ft.Text(
                    "Our Contact Details",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    font_family="Verdana",
                    color=ft.colors.GREY_800,
                ),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Row(
                                [
                                    ft.Icon(ft.icons.LOCATION_ON, color=ft.colors.PINK, size=20),
                                    ft.Text(
                                        "Address: Microkatu 1",
                                        size=16,
                                        width=700,
                                    ),
                                    
                                ],
                            ),
                            ft.Row(
                                [
                                    ft.Icon(ft.icons.PHONE, color=ft.colors.RED, size=20),
                                    ft.Text(
                                        "Phone: 041234566",
                                        size=16,
                                        width=700,
                                    ),
                                ],
                            ),
                            ft.Row(
                                [
                                    ft.Icon(ft.icons.EMAIL, color=ft.colors.BLUE, size=20),
                                    ft.Text(
                                        "Email: catbeauty@gmail.com",
                                        size=16,
                                        width=700,
                                    ),
                                ],
                            )
                        ],
                        spacing=8,
                    ) , 
                    padding=ft.padding.only(left=15),  # Add left padding to match other text alignment
                    width=700  # Match width of other text blocks      
                ),
                 ft.Text(
                    "Business Hours",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    font_family="Verdana",
                    color=ft.colors.GREY_800,
                ),
                ft.Container(
                    ft.Column(
                        [
                            ft.Text(
                                "Monday – Friday: 9:00 AM – 7:00 PM",
                                size=16,
                                weight=ft.FontWeight.NORMAL,
                                font_family="Verdana",
                                color=ft.colors.GREY_800,
                                width=700,
                            ),
                            ft.Text(
                                "Saturday: 10:00 AM – 6:00 PM",
                                size=16,
                                weight=ft.FontWeight.NORMAL,
                                font_family="Verdana",
                                color=ft.colors.GREY_800,
                                width=700,
                            ),
                            ft.Text(
                                "Sunday: Closed",
                                size=16,
                                weight=ft.FontWeight.NORMAL,
                                font_family="Verdana",
                                color=ft.colors.GREY_800,
                                width=700,
                            ),
                        ],
                        spacing = 8,
                    ),
                    width=700,
                ),

                
                # Form Fields
                ft.Row(
                    [
                        firstname,
                        lastname,
                    ],
                    spacing=20,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [
                        firstname_error,
                        lastname_error,
                    ],
                    spacing=20,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [
                        email,
                        phone,
                    ],
                    spacing=20,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [
                        email_error,
                    ],
                    spacing=20,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                message,
            
                # Submit Button without EdgeInsets
                ft.Container(
                    content=ft.ElevatedButton(
                        text="Submit",
                        on_click=handle_submit,
                        style=ft.ButtonStyle(
                            bgcolor=ft.colors.BLACK,
                            color=ft.colors.WHITE,
                            padding=20  
                        )
                    ),
                    alignment=ft.alignment.center,
                    margin=ft.margin.only(top=20, bottom=40)
                ),
            ],
           scroll=ft.ScrollMode.AUTO,  # Enable scrolling for the column
            spacing=20,  # Add consistent spacing between elements
            horizontal_alignment=ft.CrossAxisAlignment.CENTER, 
            expand=True,  # Allow the column to expand to full height
        ),
        expand=True,  # Allow the container to expand to full height
        padding=ft.padding.symmetric(horizontal=20),  # Add horizontal padding
    )