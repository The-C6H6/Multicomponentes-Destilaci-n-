from sympy import symbols, exp, log, nsolve, S

def calculos_multicomponentes(t, Pt, zif, fraccion_vapor, variable, constantes_k):
    T, P, fv = symbols('T P fv')


    if variable == "Temperatura":
        ecuacion, cadena_suma, Kis, cadena_k = ecuacion_McWilliams(
            T, Pt, zif, fraccion_vapor, constantes_k
        )
        solucion = resolver_ecuacion(ecuacion, T, "Temperatura")
        cadena_respuesta=f"Temperatura de ebullición(McWilliams): {solucion} Rankine"
        return cadena_k, cadena_suma, cadena_respuesta

    elif variable == "Presión":
        ecuacion, cadena_suma, Kis, cadena_k = ecuacion_McWilliams(
            t, P, zif, fraccion_vapor, constantes_k
        )

        solucion = resolver_ecuacion(ecuacion, P, "Presión")
        cadena_respuesta=f"Presión de ebullición(McWilliams): {solucion} psi"
        return cadena_k, cadena_suma, cadena_respuesta

    elif variable == "Fracción Vapor":
        ecuacion, cadena_suma, Kis, cadena_k = ecuacion_McWilliams(
            t, Pt, zif, fv, constantes_k
        )
        solucion = resolver_ecuacion(ecuacion, fv, "Fracción Vapor")
        cadena_respuesta=f"Fracción de vapor(McWilliams): {solucion}"
        return cadena_k, cadena_suma, cadena_respuesta


def ecuacion_McWilliams(T, P, zif, fraccion_vapor, constantes_k):
    suma = S(0)
    Kis = []

    cadena_k = "K = exp(aT1/T^2 + aT2/T + aT6 + ap1*ln(P) + ap2/P^2 + ap6/P)\n\n"
    cadena_suma = "Φ(fv) = Σ [ zif (ki - 1) / (1 + fv(ki - 1)) ] = 0\n\n"

    for i, comp in enumerate(constantes_k):
        Ki = exp(
            comp['aT1'] / T**2 +
            comp['aT2'] / T +
            comp['aT6'] +
            comp['ap1'] * log(P) +
            comp['ap2'] / P**2 +
            comp['ap6'] / P
        )

        Kis.append(Ki)

        cadena_k += (
            f"Componente {i+1}: K{i+1} = exp("
            f"{comp['aT1']}/T^2 + {comp['aT2']}/T + {comp['aT6']} + "
            f"{comp['ap1']}*ln(P) + {comp['ap2']}/P^2 + {comp['ap6']}/P)\n"
        )
        cadena_k += f"Componente {i+1}: K{i+1} = {Ki}\n"

        termino = zif[i] * (Ki - 1) / (1 + fraccion_vapor * (Ki - 1))
        suma += termino

        if i > 0:
            cadena_suma += " + \n"
        cadena_suma += f"{zif[i]} * ({Ki} - 1) / (1 + {fraccion_vapor} * ({Ki} - 1))"

    return suma, cadena_suma, Kis, cadena_k


def resolver_ecuacion(ecuacion, variable, tipo_variable):
    print(ecuacion)
    if tipo_variable == "Temperatura":
        semillas = [0, 200, 300, 500, 700, 1000, 1500]
        condicion = lambda s: s > 0

    elif tipo_variable == "Presión":
        semillas = [1, 5, 10, 20, 50, 100, 300, 1000, 5000]
        condicion = lambda s: s > 0

    elif tipo_variable == "Fracción Vapor":
        semillas = [0.001, 0.01, 0.1, 0.3, 0.5, 0.8, 0.99]
        condicion = lambda s: 0 <= s <= 1


    for x0 in semillas:
        try:
            sol = float(nsolve(ecuacion, variable, x0))
            if condicion(sol):
                return sol
        except Exception:
            continue

    return f"No se encontró solución válida para {tipo_variable}."