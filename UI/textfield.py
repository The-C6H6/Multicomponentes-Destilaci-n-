import flet as ft   
from UI import on_composicion_change, on_variable_numerica_change



def tf_composicion(estado, indice):
    return ft.TextField(
        label=f"Composición z{indice + 1}",
        width=200,
        value=estado["componentes"][indice]["composicion"],
        hint_text="Ej. 0.25",
        on_change=lambda e: on_composicion_change(e,indice, estado),
    )


def tf_variables_disponibles(var, estado):
    return ft.TextField(
        label=f"{var}",
        value=estado["Variables_valores"][var] if estado["Variables_valores"][var] is not None else "",
        width=200,
        hint_text="[Psi] o [Rankie]",
        on_change=lambda e :on_variable_numerica_change(e, var, estado)
    )