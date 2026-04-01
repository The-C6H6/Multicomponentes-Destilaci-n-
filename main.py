import flet as ft
from constantes_k import constantes_k
from UI import (
    dd_num_componentes, 
    dd_variable, 
    limpiar, 
    calcular,
    render

)





def main(page: ft.Page):
    page.title = "DESTILACIÓN DE MEZCLAS - Cálculo de Mezcla"
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 20

    estado = {
        "Variables_valores": {        
                    "Presión": None,
                    "Temperatura": None, 
                    "Fracción Vapor": None
                    },

        "n_componentes": 0,
        "constantes_k":[],
        "variable": None,
        "variables_disponibles": [],
        "componentes": [],
        "resultado_constantes": "",
        "resultado_ecuacion": "",
        "resultado_final": "",
        
                            
    }
    

    componentes_UI={
        "page": page,   
        "dropdown_num_componentes": dd_num_componentes(estado, lambda: render(componentes_UI=componentes_UI, estado=estado)),
        "dropdown_variable": dd_variable(estado, lambda: render(componentes_UI=componentes_UI, estado=estado)),
        "textfields_variables_disponibles": [],
        "filas_componentes": [],
        "controles_resultado": [],
        "dropdown_sustancia": None,
        "textfield_composicion": None,
        "boton_limpiar": ft.Button("Limpiar", on_click=lambda e: limpiar(e, estado, lambda: render(componentes_UI=componentes_UI, estado=estado))),
        "boton_calcular":ft.OutlinedButton("Calcular", on_click=lambda e: calcular(e, estado, lambda: render(componentes_UI=componentes_UI, estado=estado)))
    }


    render(componentes_UI=componentes_UI, estado=estado )


ft.run(main)