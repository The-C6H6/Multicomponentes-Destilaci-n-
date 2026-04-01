import flet as ft
from constantes_k import constantes_k   
from .acciones import on_variable_change, on_sustancia_change
from .acciones import on_num_componentes_change



def dd_num_componentes(estado: dict, render: callable) -> ft.Dropdown :
    return ft.Dropdown(
            label="¿Cuántos componentes tiene la mezcla?",
            width=500,
            value=str(estado["n_componentes"]) if estado["n_componentes"] else None,
            options=[ft.dropdown.Option(str(i)) for i in range(1, 11)],
            on_select=lambda e: on_num_componentes_change(e, estado, render),
        )

def dd_sustancia(i: int, comp, estado) -> ft.Dropdown:
    return ft.Dropdown(
                label=f"Sustancia {i}",
                width=300,
                value=comp["sustancia"],
                options=[
                    ft.dropdown.Option(nombre)
                    for nombre in sorted(constantes_k.keys())
                ],
                on_select=lambda e, idx=i - 1: on_sustancia_change(e, idx, estado),
            )

def dd_variable(estado: dict, render: callable) -> ft.Dropdown:   
    return ft.Dropdown(
            label="Selecciona la variable",
            width=500,
            value=estado["variable"],
            options=[
                ft.dropdown.Option("Temperatura"),
                ft.dropdown.Option("Presión"),
                ft.dropdown.Option("Fracción Vapor"),
            ],
            on_select=lambda e: on_variable_change(e, estado, render),
        )






