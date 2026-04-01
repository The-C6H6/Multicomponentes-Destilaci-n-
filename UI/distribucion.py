import flet as ft

def distribuir_componentes(estado, componentes_UI):
     return ft.Column(
                controls=[
                    ft.Text("Cálculo de mezcla", size=24, weight=ft.FontWeight.BOLD),
                    ft.Row(
                        controls=[componentes_UI["dropdown_num_componentes"], componentes_UI["dropdown_variable"]],
                        spacing=20,
                        wrap=True,
                    ),
                    ft.Divider(),
                    ft.Column(controls=componentes_UI["textfields_variables_disponibles"], spacing=12),
                    ft.Column(controls=componentes_UI["filas_componentes"], spacing=12),
                    ft.Row(
                        controls=[
                            componentes_UI["boton_limpiar"],
                            componentes_UI["boton_calcular"]
                        ],
                        spacing=15,
                    ),
                    ft.Divider(),
                    ft.Column(controls=componentes_UI["controles_resultado"], spacing=15),
                ],
                spacing=18,
            )