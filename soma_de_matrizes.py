
matriz1 = [[1,42,3],[1,4,2],[9,3,55]]
matriz2 = [[99,3,3],[11,44,12],[9,32,5]]


def soma_matrizes(matriz1, matriz2):
    matriz_soma=[]
    for row in matriz1:
        linha_soma = [number+matriz2[matriz1.index(row)][row.index(number)] for number in row]

        matriz_soma.append(linha_soma)
    return matriz_soma

matriz = soma_matrizes(matriz1, matriz2)

for row in matriz:
    print(row)
