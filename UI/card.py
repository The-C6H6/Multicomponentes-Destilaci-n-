import flet as ft



def crear_card(titulo: str, contenido: str) -> ft.Card:
    return ft.Card(
        content=ft.Container(
            padding=15,
            width=900,
            content=ft.Column(
                controls=[
                    ft.Text(titulo, size=18, weight=ft.FontWeight.BOLD),
                    ft.Text(
                        contenido,
                        selectable=True,
                        size=15,
                        font_family="Courier New",
                    ),
                ],
                spacing=10,
            ),
        )
    )