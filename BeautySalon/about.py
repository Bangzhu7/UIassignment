import flet as ft
import os

def AboutPage():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    assets_path = os.path.join(current_dir, "assets")
    image_path = os.path.join(assets_path, "picture1.png")

    return ft.Container(
        content=ft.Column(
            [
                ft.Text('About', 
                    size=60,
                    weight=ft.FontWeight.W_500,
                    font_family="Verdana",
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Text(
                    "Welcome to Beuty Salon",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    font_family="Verdana",
                    color=ft.colors.GREY_700,
                ),
                ft.Text(
                    "At Beauty Salon, we believe that beauty is more than skin deep—it's about confidence, self-care, and celebrating your unique style. Our mission is to provide exceptional beauty and wellness services in a relaxing, luxurious environment.",
                    size=16,
                    weight=ft.FontWeight.NORMAL,
                    font_family="Verdana",
                    color=ft.colors.GREY_700,
                    width=700
                ),
                ft.Text(
                    "Our Story",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    font_family="Verdana",
                    color=ft.colors.GREY_700,
                ),    
                ft.Text(
                    "Founded in 2024, Beauty Salon has been a trusted destination for Kuopio residents seeking expert care for hair, skin, and nails. With a team of highly trained professionals passionate about their craft, we take pride in delivering personalized treatments tailored to meet your needs.",
                    size=16,
                    weight=ft.FontWeight.NORMAL,
                    font_family="Verdana",
                    color=ft.colors.GREY_700,
                    width=700
                ),
                ft.Text(
                    "Our Services",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    font_family="Verdana",
                    color=ft.colors.GREY_700,
                ),           
                ft.Text(
                    "From precision haircuts and creative coloring to rejuvenating facials and nail artistry, we offer a full range of services designed to make you look and feel your best. Our salon uses only the highest-quality products, ensuring your beauty treatments are both effective and sustainable.",
                    size=16,
                    weight=ft.FontWeight.NORMAL,
                    font_family="Verdana",
                    color=ft.colors.GREY_700,
                    width=700
                ),
                ft.Text(
                    "Why Choose Us?",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    font_family="Verdana",
                    color=ft.colors.GREY_700,
                ),        
                # Container for the bulleted list with proper indentation
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Row(
                                [
                                    ft.Icon(ft.icons.CIRCLE, size=8), 
                                    ft.Text(
                                        "A team of skilled and certified professionals.", 
                                        font_family="Vernada", 
                                        size=16,
                                        width=700  # Adjusted width to match other text blocks
                                    )
                                ],
                                spacing=10
                            ),
                            ft.Row(
                                [
                                    ft.Icon(ft.icons.CIRCLE, size=8), 
                                    ft.Text(
                                        "A commitment to the latest trends, techniques, and technology in beauty care.", 
                                        font_family="Vernada", 
                                        size=16,
                                        width=700
                                    )
                                ],
                                spacing=10
                            ),
                            ft.Row(
                                [
                                    ft.Icon(ft.icons.CIRCLE, size=8), 
                                    ft.Text(
                                        "A warm, welcoming atmosphere where you can unwind and be pampered.", 
                                        font_family="Vernada", 
                                        size=16,
                                        width=700
                                    )
                                ],
                                spacing=10
                            ),
                        ],
                        spacing=8,
                    ),
                    padding=ft.padding.only(left=15),  # Add left padding to match other text alignment
                    width=700  # Match width of other text blocks
                ),    
                ft.Text(
                    "Let Us Pamper You",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    font_family="Verdana",
                    color=ft.colors.GREY_700,
                ),
                ft.Text(
                    "Whether you're here for a quick touch-up or a complete makeover, our goal is to leave you glowing with confidence. Visit Beauty Salon and experience the art of beauty done right.",
                    size=16,
                    font_family="Verdana",
                    color=ft.colors.GREY_700,
                    width=700
                ),    
                ft.Container(
                    content=ft.Image(
                        src=image_path,
                        width=700,
                        height=400,
                        fit=ft.ImageFit.COVER,
                    ),
                    margin=ft.margin.only(top=20),
                    border_radius=10
                )
            ],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        padding=ft.padding.only(top=40),
        alignment=ft.alignment.center
    )