from constantes_k import constantes_k
from calculos import calculos_multicomponentes


def on_composicion_change(e, indice, estado):
        estado["componentes"][indice]["composicion"] = e.control.value
        
def on_variable_change(e, estado, render):
    estado["Variables_valores"]["Temperatura"] = None
    estado["Variables_valores"]["Presión"] = None
    estado["Variables_valores"]["Fracción Vapor"] = None
    estado["variable"] = e.control.value
    print(f"Variable seleccionada: {estado['variable']}")
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
        estado["constantes_k"] = []
        for i, comp in enumerate(estado["componentes"], start=1):
            if not comp["sustancia"] or not comp["composicion"]:
                return  
            sustancia = comp["sustancia"]
            composicion = comp["composicion"]

            datos = constantes_k[sustancia]
            estado["constantes_k"].append({
                "sustancia": sustancia,
                "composicion": composicion,
                "aT1": datos["aT1"],
                "aT2": datos["aT2"],
                "aT6": datos["aT6"],
                "ap1": datos["ap1"],
                "ap2": datos["ap2"],
                "ap6": datos["ap6"],
                "error_medio": datos["error_medio"]
            })
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
        cadena_k, cadena_suma, cadena_respuesta= calculos_multicomponentes(
            t=estado["Variables_valores"]["Temperatura"],
            Pt=estado["Variables_valores"]["Presión"],
            zif=[float(comp["composicion"]) for comp in estado["componentes"]],
            fraccion_vapor=estado["Variables_valores"]["Fracción Vapor"],
            constantes_k=estado["constantes_k"],
            variable=estado["variable"]
        )
        estado["resultado_ecuacion"] = cadena_k + "\n\n" + cadena_suma
        estado["resultado_final"] = cadena_respuesta

        if not estado["variable"]:
              return
        

        render()