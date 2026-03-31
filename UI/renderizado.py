from UI import dd_num_componentes, dd_sustancia, dd_variable, crear_card, distribuir_componentes, limpiar, calcular, on_variable_change, on_sustancia_change, on_composicion_change, ajustar_lista_componentes, on_num_componentes_change, tf_composicion 
import flet as ft

def render(componentes_UI, estado):
        componentes_UI["page"].controls.clear()
        componentes_UI["filas_componentes"]=[]
        componentes_UI["controles_resultado"]=[]    
        for i, comp in enumerate(estado["componentes"], start=1):
            componentes_UI["dropdown_sustancia"] = dd_sustancia(i, comp, estado)
            componentes_UI["textfield_composicion"] = tf_composicion(estado, i-1)

            componentes_UI["filas_componentes"].append(
                ft.Row(
                    controls=[componentes_UI["dropdown_sustancia"], componentes_UI["textfield_composicion"]],
                    spacing=15,
                    wrap=True,
                )
            )

        

        if estado["resultado_constantes"]:
            componentes_UI["controles_resultado"].append(
                crear_card("Constantes", estado["resultado_constantes"])
            )

        if estado["resultado_ecuacion"]:
            componentes_UI["controles_resultado"].append(
                crear_card("Ecuación", estado["resultado_ecuacion"])
            )

        if estado["resultado_final"]:
            componentes_UI["controles_resultado"].append(
                crear_card("Resultados", estado["resultado_final"])
            )

        componentes_UI["page"].add(
            distribuir_componentes(estado, componentes_UI)
        )

        componentes_UI["page"].update()