def numero_a_literal(numero):
    unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    especiales = ["diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve"]
    decenas = ["", "diez", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
    centenas = ["", "ciento", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]

    def convertir_grupo(numero):
        if numero == 0:
            return ""
        elif numero < 10:
            return unidades[numero]
        elif numero < 20:
            return especiales[numero - 10]
        elif numero < 100:
            decena = numero // 10
            unidad = numero % 10
            if unidad == 0:
                return decenas[decena]
            else:
                return decenas[decena] + " y " + unidades[unidad]
        elif numero < 1000:
            centena = numero // 100
            resto = numero % 100
            if resto == 0:
                return centenas[centena]
            else:
                return centenas[centena] + " " + convertir_grupo(resto)
        elif numero < 1000000:
            miles_parte = numero // 1000
            resto_miles = numero % 1000
            if resto_miles == 0:
                return convertir_grupo(miles_parte) + " mil"
            elif resto_miles < 100:
                return convertir_grupo(miles_parte) + " mil " + convertir_grupo(resto_miles)
            else:
                return convertir_grupo(miles_parte) + " mil " + convertir_grupo(resto_miles)
        elif numero < 1000000000:
            millones_parte = numero // 1000000
            resto_millones = numero % 1000000
            if resto_millones == 0:
                return convertir_grupo(millones_parte) + " millones"
            elif resto_millones < 1000:
                return convertir_grupo(millones_parte) + " millones " + convertir_grupo(resto_millones)
            else:
                return convertir_grupo(millones_parte) + " millones " + convertir_grupo(resto_millones)

    if numero == 0:
        return "cero"
    elif numero < 1000000000:
        return convertir_grupo(numero)

if __name__ == "__main__":
    try:
        numero_usuario = int(input("Introduce un número entero: "))
        if numero_usuario < 0:
            print("Por favor, introduce un número positivo.")
        else:
            resultado = numero_a_literal(numero_usuario)
            print(resultado)
    except ValueError:
        print("Error: Por favor, introduce un número válido.")
