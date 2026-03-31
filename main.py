import flet as ft
from constantes_k import constantes_k
from UI import (
    crear_card, 
    dd_num_componentes, 
    dd_sustancia, 
    dd_variable, 
    tf_composicion,
    distribuir_componentes,
    limpiar, 
    calcular,

)





def main(page: ft.Page):
    page.title = "DESTILACIÓN DE MEZCLAS - Cálculo de Mezcla"
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
    
        

    def render():
        page.controls.clear()
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

        page.add(
            distribuir_componentes(estado, componentes_UI)
        )

        page.update()


    componentes_UI={
        "dropdown_num_componentes": dd_num_componentes(estado, render),
        "dropdown_variable": dd_variable(estado),
        "filas_componentes": [],
        "controles_resultado": [],
        "dropdown_sustancia": None,
        "textfield_composicion": None,
        "boton_limpiar": ft.OutlinedButton("Limpiar", on_click=lambda e: limpiar(e, estado, render)),
        "boton_calcular":ft.ElevatedButton("Calcular", on_click=lambda e: calcular(e, estado, render))
    }








    render()


ft.app(target=main)