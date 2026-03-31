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
    render

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
    

    componentes_UI={
        "page": page,   
        "dropdown_num_componentes": dd_num_componentes(estado, lambda: render(componentes_UI=componentes_UI, estado=estado)),
        "dropdown_variable": dd_variable(estado),
        "filas_componentes": [],
        "controles_resultado": [],
        "dropdown_sustancia": None,
        "textfield_composicion": None,
        "boton_limpiar": ft.OutlinedButton("Limpiar", on_click=lambda e: limpiar(e, estado, lambda: render(componentes_UI=componentes_UI, estado=estado))),
        "boton_calcular":ft.ElevatedButton("Calcular", on_click=lambda e: calcular(e, estado, lambda: render(componentes_UI=componentes_UI, estado=estado)))
    }


    render(componentes_UI=componentes_UI, estado=estado )


ft.app(target=main)