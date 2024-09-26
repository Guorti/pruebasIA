def resolucy(refutacion):
    """
    Algoritmo de Resoluci n por Refutaci n
    """
    # Crear una lista para almacenar las clausulas
    clausulas = []
    # Agregar las clausulas a la lista
    clausulas.extend(refutacion)
    # Iterar sobre las clausulas
    while clausulas:
        # Extraer la primera clausula
        clausula = clausulas.pop(0)
        # Iterar sobre las clausulas restantes
        for otra_clausula in clausulas[1:]:
            # Verificar si se pueden resolver
            if clausula[0] == otra_clausula[1] and clausula[1] == otra_clausula[0]:
                # Crear una nueva clausula sin las literales resueltas
                nueva_clausula = [lit for lit in clausula + otra_clausula if lit not in [clausula[0], otra_clausula[1]]]
                # Agregar la nueva clausula a la lista
                clausulas.append(nueva_clausula)
    # Verificar si se resolvi o
    if not clausulas:
        return True
    else:
        return False


# Recuerde, si llega clausula vacia es verdadero
# Validaci n
refutacion = [["P","∨", "Q"], "∧", ["~Q"]]
hipotesis = ["~P"]
print(resolucy(refutacion))