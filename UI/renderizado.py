from UI import dd_sustancia, crear_card, distribuir_componentes, tf_composicion, tf_variables_disponibles
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
        estado["variables_disponibles"] = []
        if estado["variable"]:
             componentes_UI["textfields_variables_disponibles"] = []
             variables_posibles = ["Temperatura", "Presión", "Fracción Vapor"]
             variables_posibles.remove(estado["variable"])
             estado["variables_disponibles"] = variables_posibles
        for var in estado["variables_disponibles"]:
            componentes_UI["textfields_variables_disponibles"].append(
                tf_variables_disponibles(var, estado)
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