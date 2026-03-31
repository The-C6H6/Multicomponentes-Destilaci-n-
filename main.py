import flet as ft
from constantes_k import constantes_k


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


def main(page: ft.Page):
    page.title = "Mezclas"
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 20

    estado = {
        "n_componentes": 0,
        "variable": None,
        "componentes": [],
        "resultado_constantes": "",
        "resultado_ecuacion": "",
        "resultado_final": "",
    }

    def mostrar_mensaje(texto: str):
        page.snack_bar = ft.SnackBar(ft.Text(texto))
        page.snack_bar.open = True
        page.update()

    def ajustar_lista_componentes(n: int):
        actuales = len(estado["componentes"])

        if n > actuales:
            for _ in range(n - actuales):
                estado["componentes"].append(
                    {
                        "sustancia": None,
                        "composicion": "",
                    }
                )
        elif n < actuales:
            estado["componentes"] = estado["componentes"][:n]

    def on_num_componentes_change(e):
        valor = e.control.value

        if valor:
            estado["n_componentes"] = int(valor)
        else:
            estado["n_componentes"] = 0

        ajustar_lista_componentes(estado["n_componentes"])

        estado["resultado_constantes"] = ""
        estado["resultado_ecuacion"] = ""
        estado["resultado_final"] = ""

        render()

    def on_variable_change(e):
        estado["variable"] = e.control.value
        render()

    def on_sustancia_change(e, indice):
        estado["componentes"][indice]["sustancia"] = e.control.value

    def on_composicion_change(e, indice):
        estado["componentes"][indice]["composicion"] = e.control.value

    def calcular(e):
        if estado["n_componentes"] == 0:
            mostrar_mensaje("Selecciona cuántos componentes tiene la mezcla.")
            return

        if not estado["variable"]:
            mostrar_mensaje("Selecciona una variable.")
            return

        texto_constantes = []

        for i, comp in enumerate(estado["componentes"], start=1):
            sustancia = comp["sustancia"]
            composicion = comp["composicion"]

            if not sustancia or not composicion:
                mostrar_mensaje(f"Completa la sustancia y composición del componente {i}.")
                return

            datos = constantes_k[sustancia]

            bloque = (
                f"Componente {i}: {sustancia}\n"
                f"z{i} = {composicion}\n"
                f"aT1 = {datos['aT1']}\n"
                f"aT2 = {datos['aT2']}\n"
                f"aT6 = {datos['aT6']}\n"
                f"ap1 = {datos['ap1']}\n"
                f"ap2 = {datos['ap2']}\n"
                f"ap6 = {datos['ap6']}\n"
                f"error_medio = {datos['error_medio']}"
            )
            texto_constantes.append(bloque)

        estado["resultado_constantes"] = "\n\n".join(texto_constantes)
        estado["resultado_ecuacion"] = "𝛷(fv) = ∑[(zi(ki−1)) / (1 + fv(ki−1))] = 0"

        mapa_resultado = {
            "Temperatura": "T",
            "Presión": "P",
            "Fracción Vapor": "fv",
        }

        estado["resultado_final"] = mapa_resultado[estado["variable"]]

        render()

    def limpiar(e):
        estado["n_componentes"] = 0
        estado["variable"] = None
        estado["componentes"] = []
        estado["resultado_constantes"] = ""
        estado["resultado_ecuacion"] = ""
        estado["resultado_final"] = ""
        render()

    def render():
        page.controls.clear()

        dropdown_num_componentes = ft.Dropdown(
            label="¿Cuántos componentes tiene la mezcla?",
            width=500,
            value=str(estado["n_componentes"]) if estado["n_componentes"] else None,
            options=[ft.dropdown.Option(str(i)) for i in range(1, 11)],
            on_select=on_num_componentes_change,
        )

        dropdown_variable = ft.Dropdown(
            label="Selecciona la variable",
            width=500,
            value=estado["variable"],
            options=[
                ft.dropdown.Option("Temperatura"),
                ft.dropdown.Option("Presión"),
                ft.dropdown.Option("Fracción Vapor"),
            ],
            on_select=on_variable_change,
        )

        filas_componentes = []

        for i, comp in enumerate(estado["componentes"], start=1):
            dropdown_sustancia = ft.Dropdown(
                label=f"Sustancia {i}",
                width=300,
                value=comp["sustancia"],
                options=[
                    ft.dropdown.Option(nombre)
                    for nombre in sorted(constantes_k.keys())
                ],
                on_select=lambda e, idx=i - 1: on_sustancia_change(e, idx),
            )

            textfield_composicion = ft.TextField(
                label=f"Composición z{i}",
                width=200,
                value=comp["composicion"],
                hint_text="Ej. 0.25",
                on_change=lambda e, idx=i - 1: on_composicion_change(e, idx),
            )

            filas_componentes.append(
                ft.Row(
                    controls=[dropdown_sustancia, textfield_composicion],
                    spacing=15,
                    wrap=True,
                )
            )

        controles_resultado = []

        if estado["resultado_constantes"]:
            controles_resultado.append(
                crear_card("Constantes", estado["resultado_constantes"])
            )

        if estado["resultado_ecuacion"]:
            controles_resultado.append(
                crear_card("Ecuación", estado["resultado_ecuacion"])
            )

        if estado["resultado_final"]:
            controles_resultado.append(
                crear_card("Resultados", estado["resultado_final"])
            )

        page.add(
            ft.Column(
                controls=[
                    ft.Text("Cálculo de mezcla", size=24, weight=ft.FontWeight.BOLD),
                    ft.Row(
                        controls=[dropdown_num_componentes, dropdown_variable],
                        spacing=20,
                        wrap=True,
                    ),
                    ft.Divider(),
                    ft.Column(controls=filas_componentes, spacing=12),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton("Calcular", on_click=calcular),
                            ft.OutlinedButton("Limpiar", on_click=limpiar),
                        ],
                        spacing=15,
                    ),
                    ft.Divider(),
                    ft.Column(controls=controles_resultado, spacing=15),
                ],
                spacing=18,
            )
        )

        page.update()

    render()


ft.app(target=main)