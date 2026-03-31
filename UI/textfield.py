import flet as ft   
from UI import on_composicion_change



def tf_composicion(estado, indice):
    return ft.TextField(
        label=f"Composición z{indice + 1}",
        width=200,
        value=estado["componentes"][indice]["composicion"],
        hint_text="Ej. 0.25",
        on_change=lambda e: on_composicion_change(e,indice, estado),
    )



