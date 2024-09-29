def agregar_simbolo_negacion(s):
    """
    Agrega el simbolo de negacion "~" a una string
    """
    if s.startswith("~"):
        return s[1:]
    else:
        return "~" + s

def resolucy(refutacion, hipoth):
    """
    Algoritmo de Resoluci n por Refutaci n
    """
    # Crear una lista para almacenar las clausulas e hipotesis
    clausulas_refutacion = []
    hipotesis = []
    # Agregar las clausulas a la lista
    clausulas_refutacion.extend(refutacion)
    hipotesis.extend(hipoth)
    # Remover el simbolo de negacion de la hipotesis YA ESCRITA ABAJO
    hipotesisParaComparacion = hipotesis[0][1:]
    # Iterar sobre las clausulas    
    # Extraer la primera clausula de la lista de clausulas totales
    #clausula = clausulas_refutacion.pop(0)

    i=0
    while clausulas_refutacion:
        while i < len(clausulas_refutacion):
            #For que recorre todos los items individuales de la clausula
            j = 0
            while j < len(clausulas_refutacion[i]):
                a = clausulas_refutacion[i][j]
                if hipotesisParaComparacion == clausulas_refutacion[i][j]:
                # Revisar el tamano de la clausula para saber si es una clausula de un solo item
                    if len(clausulas_refutacion[i]) < 3:
                        if clausulas_refutacion[i][j] != '∧' or clausulas_refutacion[i][j] != '∨':
                            #FALTA LOGICA PARA UNIR DOS CLAUSULAS POR OPERADOR
                            # La clausula con la que comparamos se convierte en el item unico de la clausula
                            #Y se elimina de la lista de clausulas
                            hipotesisParaComparacion = agregar_simbolo_negacion(clausulas_refutacion[i][j])
                            clausulas_refutacion.pop(i)
                            i=0
                            if len(clausulas_refutacion) == 0:
                                return True
                            continue
                        else:
                            clausulas_refutacion.pop(i)
                            i=0
                            if len(clausulas_refutacion) == 0:
                                return True
                            continue
                #Si la clausula es de 3 items, esta contiene un operador dentro, por lo que se evalua
                    if len(clausulas_refutacion[i]) == 3:
                        # Si el comparador es "OR", tratamos cada item de manera individual
                        # Revisamos el indice 1, porque es el operador entre la operacion binaria
                        if clausulas_refutacion[i][1] == "∨":
                            # Comparar la hipotesis con la clausula, si hay terminos iguales, se resuelve
                            # Recordando que estamos operando dos clausulas entre si por la binariedad de la matematica
                            if hipotesisParaComparacion == clausulas_refutacion[i][0]:
                                hipotesisParaComparacion = agregar_simbolo_negacion(clausulas_refutacion[i][2])
                                clausulas_refutacion.pop(i)
                                #Si encuentra un item con que anular la hipotesis actual, devuelve i a 0, para evaluar la primer clausula
                                #Debido a que estamos haciendo pop
                                i=0
                                if len(clausulas_refutacion) == 0:
                                    return True
                                continue
                            if hipotesisParaComparacion == clausulas_refutacion[i][2]:
                                hipotesisParaComparacion = agregar_simbolo_negacion(clausulas_refutacion[i][0])
                                clausulas_refutacion.pop(i)
                                #Si encuentra un item con que anular la hipotesis actual, devuelve i a 0, para evaluar la primer clausula
                                #Debido a que estamos haciendo pop
                                i=0
                                if len(clausulas_refutacion) == 0:
                                    return True
                                continue
                        #FALTA VALIDAR EL RESTO DE OPERADORES  
                if clausulas_refutacion[i][j] == '∧' or clausulas_refutacion[i][j] == '∨':
                    i=0
                    clausulas_refutacion.pop(i)
                else:
                    #Si no lo encuentra, busca en el siguiente item de la clausula
                    j=j+1
            #Si no encuentra una concordancia dentro de los items de la clausula, pasa la siguiente.
            i=i+1

        return False
        

# Recuerde, si llega clausula vacia es verdadero
# Validacion
refutacion = [["P","∨", "Q"], ["∧"], ["~Q"]]
hipoth = ["~P"]
print(resolucy(refutacion, hipoth))