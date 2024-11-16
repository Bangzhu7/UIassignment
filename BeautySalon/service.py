import flet as ft

def ServicePage(page):
    # Set page properties
    page.title = "Our Services"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = 30
    page.spacing = 20

    # Define service data
    services = [
        {"name": "Wash & Dry", "duration": "1 hr", "price": "$100"},
        {"name": "Trim", "duration": "1 hr", "price": "$35"},
        {"name": "Cut & Blow Dry", "duration": "1 hr", "price": "$50"},
        {"name": "Cut & Blow Dry", "duration": "1 hr", "price": "$50"},
    ]

    # Title text
    title = ft.Text("Our Services", size=40, weight=ft.FontWeight.BOLD)

    # List to hold service rows
    service_rows = []

    for service in services:
        # Service name and duration
        service_name = ft.Text(service["name"], size=20)
        duration_price = ft.Column([
            ft.Text(service["duration"], size=14),
            ft.Text(service["price"], size=14),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)

        # Book Now button
        book_button = ft.ElevatedButton(
            "Book Now",
            bgcolor=ft.colors.BLACK,
            color=ft.colors.WHITE,
            # on_click=lambda e, service=service: print(f"Booked {service['name']}"),
            on_click=lambda _: page.go("/book_calendar"),
        )

        # Row layout for each service
        row = ft.Row(
            [
                ft.Column([service_name], expand=True),
                duration_price,
                book_button,
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            height=60,
        )
        
        # Add separator and row
        service_rows.append(ft.Divider(height=1, color=ft.colors.BLACK12))
        service_rows.append(row)

    # Footer text
    footer = ft.Text(
        "Designed by Fozle Arafat",
        size=12,
        color=ft.colors.BLACK54,
        italic=True,
        text_align=ft.TextAlign.CENTER
    )

    # Add elements to page
    return ft.Container(
        content=ft.Column(
            [
                title,
                *service_rows,
                ft.Divider(height=1, color=ft.colors.BLACK12),  # Final separator
                footer  # Footer at the end
            ],
            spacing=20
        ),
        padding=20
    )


        