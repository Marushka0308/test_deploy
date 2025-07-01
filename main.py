import flet as ft
import os


def main(page: ft.Page):
    # Set page properties
    page.title = "My First Flet App"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Create a counter variable
    counter = ft.Text("0", size=50, color=ft.colors.BLUE)

    def increment_counter(e):
        counter.value = str(int(counter.value) + 1)
        page.update()

    def decrement_counter(e):
        counter.value = str(int(counter.value) - 1)
        page.update()

    # Create the UI
    page.add(
        ft.Column([
            ft.Text("Welcome to Flet!", size=30, weight=ft.FontWeight.BOLD),
            ft.Text("Simple Counter App", size=20, color=ft.colors.GREY_700),
            ft.Container(height=20),  # Spacer
            counter,
            ft.Container(height=20),  # Spacer
            ft.Row([
                ft.ElevatedButton("➖", on_click=decrement_counter, width=100),
                ft.Container(width=20),  # Spacer
                ft.ElevatedButton("➕", on_click=increment_counter, width=100),
            ], alignment=ft.MainAxisAlignment.CENTER),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )


if __name__ == "__main__":
    # Get port from environment variable (for cloud deployment)
    port = int(os.environ.get("PORT", 8000))
    ft.app(target=main, view=ft.WEB_BROWSER, port=port, host="0.0.0.0")