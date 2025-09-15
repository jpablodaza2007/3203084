from collections import Counter
import heapq

class NodoHuffman:
    """Nodo para el árbol de codificación Huffman"""
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def comprimir_repeticion_simple(texto):
    """
    Compresión simple: reemplaza secuencias repetidas
    Ejemplo: "aaaa" -> "4a"
    """
    if not texto:
        return ""
    comprimido = []
    conteo = 1
    for i in range(1, len(texto)):
        if texto[i] == texto[i - 1]:
            conteo += 1
        else:
            comprimido.append(f"{conteo}{texto[i - 1]}")
            conteo = 1
    comprimido.append(f"{conteo}{texto[-1]}")
    return "".join(comprimido)

def descomprimir_repeticion_simple(texto):
    numero = ""
    descomprimido = []
    for char in texto:
        if char.isdigit():
            numero += char
        else:
            cantidad = int(numero) if numero else 1
            descomprimido.append(char * cantidad)
            numero = ""
    return "".join(descomprimido)

def construir_arbol_huffman(texto):
    frecuencia = Counter(texto)
    heap = [NodoHuffman(char, freq) for char, freq in frecuencia.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        izquierda = heapq.heappop(heap)
        derecha = heapq.heappop(heap)
        nodo_combinado = NodoHuffman(None, izquierda.freq + derecha.freq, izquierda, derecha)
        heapq.heappush(heap, nodo_combinado)
    return heap[0]

def generar_codigos_huffman(nodo, codigo="", codigos=None):
    if codigos is None:
        codigos = {}
    if nodo:
        if nodo.char is not None:
            codigos[nodo.char] = codigo
        generar_codigos_huffman(nodo.left, codigo + "0", codigos)
        generar_codigos_huffman(nodo.right, codigo + "1", codigos)
    return codigos

def comprimir_huffman(texto):
    if not texto:
        return "", {}
    raiz = construir_arbol_huffman(texto)
    codigos = generar_codigos_huffman(raiz)
    comprimido = "".join(codigos[char] for char in texto)
    return comprimido, codigos

def descomprimir_huffman(cadena_binaria, codigos):
    if not cadena_binaria or not codigos:
        return ""
    codigo_inverso = {v: k for k, v in codigos.items()}
    actual = ""
    descomprimido = []
    for bit in cadena_binaria:
        actual += bit
        if actual in codigo_inverso:
            descomprimido.append(codigo_inverso[actual])
            actual = ""
    return "".join(descomprimido)

if __name__ == "__main__":
    texto = "aaabbbbcccdde"
    print("Texto original:", texto)

    comprimido_simple = comprimir_repeticion_simple(texto)
    print("Compresión por repetición simple:", comprimido_simple)
    print("Descompresión:", descomprimir_repeticion_simple(comprimido_simple))

    comprimido_huffman, codigos = comprimir_huffman(texto)
    print("Compresión Huffman:", comprimido_huffman)
    print("Códigos Huffman:", codigos)
    print("Descompresión:", descomprimir_huffman(comprimido_huffman, codigos))
