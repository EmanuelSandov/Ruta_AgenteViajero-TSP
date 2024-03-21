Datos = {("A", "B", 9), ("A", "J", 22), ("A", "E", 15),
         ("B", "A", 9), ("B", "C", 11), ("B", "E", 17),
         ("C", "B", 11), ("C", "D", 19),
         ("D", "C", 19), ('D', "E", 15), ("D", "F", 14),
         ("E", "A", 15), ("E", "B", 17), ("E", "D", 15), ("E", "G", 14), ("E", "H", 16),
         ("F", "D", 14), ("F", "H", 15), ("F", "I", 12),
         ("G", "E", 14), ("G", "K", 14), ("G", "L", 25),
         ("H", "E", 16), ("H", "F", 15), ("H", "I", 15), ("H", "L", 17),
         ("I", "H", 15), ("I", "F", 12), ("I", "M", 19),
         ("J", "K", 6), ("J", "A", 22),
         ("K", "J", 6), ("K", "N", 14), ("K", "G", 14),
         ("L", "N", 18), ("L", "G", 25), ("L", "H", 17), ("L", "M", 18),
         ("M", "I", 19), ("M", "L", 18), ("M", "N", 24),
         ("N", "K", 14), ("N", "L", 18), ("N", "M", 24)}

def Convertir_grafo(datos):  # Convertir los datos en una estructura de grafo
    grafo = {}
    for inicio, fin, costo in datos:
        if inicio not in grafo:
            grafo[inicio] = []
        grafo[inicio].append((fin, costo))
    return grafo


grafo_costo = Convertir_grafo(Datos)


def Encontrar_Ruta(nodo, grafo, visitados, camino, costo_actual, caminos_encontrados):
    visitados.add(nodo)
    if len(camino) > 0:  # Si el camino ya tiene nodos, agregar el nodo actual al camino
        camino_actual = camino + [nodo]
    else:  # Si es el primer nodo, iniciar el camino con él
        camino_actual = [nodo]

    # Si se han visitado todos los nodos y hay un retorno al nodo de origen
    if len(visitados) == len(grafo) and nodo in grafo and any(n == camino[0] for n, _ in grafo[nodo]):
        for vecino, c in grafo[nodo]:
            if vecino == camino[0]:  # Cerrar el ciclo
                caminos_encontrados.append((camino_actual + [vecino], costo_actual + c))
    else:
        for vecino, c in grafo.get(nodo, []):
            if vecino not in visitados:
                Encontrar_Ruta(vecino, grafo, set(visitados), camino_actual, costo_actual + c, caminos_encontrados)


def Imprimir_Result(origen, grafo):
    caminos_encontrados = []
    Encontrar_Ruta(origen, grafo, set(), [], 0, caminos_encontrados)
    camino_menor_costo = None
    costo_menor = float('inf')

    if caminos_encontrados:
        print("Todos las Rutas posibles:")
        for camino, costo in caminos_encontrados:
            print(f"Camino: {' -> '.join(camino)} con un costo total de {costo}")
            if costo < costo_menor:
                costo_menor = costo
                camino_menor_costo = camino
        print("\nLa ruta más corta es:")
        print(f"{' -> '.join(camino_menor_costo)} con un costo total de {costo_menor}")
    else:
        print(f"No se encontraron tours Hamiltonianos que comiencen en {origen}")


Imprimir_Result("A", grafo_costo)
