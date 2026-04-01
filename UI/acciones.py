from constantes_k import constantes_k



def on_composicion_change(e, indice, estado):
        estado["componentes"][indice]["composicion"] = e.control.value
        
def on_variable_change(e, estado, render):
    estado["Variables_valores"]["Temperatura"] = None
    estado["Variables_valores"]["Presión"] = None
    estado["Variables_valores"]["Fracción Vapor"] = None
    estado["variable"] = e.control.value
    render()

def on_variable_numerica_change(e, var, estado):
        valor = e.control.value
        if valor:
            try:
                estado["Variables_valores"][var] = float(valor)
            except ValueError:
                estado["Variables_valores"][var] = None
        else:
            estado["Variables_valores"][var] = None
        



def on_sustancia_change(e, indice, estado):
        estado["componentes"][indice]["sustancia"] = e.control.value

def on_num_componentes_change(e, estado, render):
        valor = e.control.value        
        if valor:
            estado["n_componentes"] = int(valor)
        else:
            estado["n_componentes"] = 0

        ajustar_lista_componentes(estado["n_componentes"], estado)

        estado["resultado_constantes"] = ""
        estado["resultado_ecuacion"] = ""
        estado["resultado_final"] = ""
        render()



def ajustar_lista_componentes(n: int, estado: dict):
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





def limpiar(e, estado, render):
        #estado["componentes"] = []
        estado["resultado_constantes"] = ""
        estado["resultado_ecuacion"] = ""
        estado["resultado_final"] = ""
        render()



def calcular(e, estado, render):
        if estado["n_componentes"] == 0 or not estado["variable"]:
            return
        
        texto_constantes = []

        for i, comp in enumerate(estado["componentes"], start=1):
            if not comp["sustancia"] or not comp["composicion"]:
                return  
            sustancia = comp["sustancia"]
            composicion = comp["composicion"]

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
        if not estado["variable"]:
              return
        
        estado["resultado_final"] = mapa_resultado[estado["variable"]]

        render()