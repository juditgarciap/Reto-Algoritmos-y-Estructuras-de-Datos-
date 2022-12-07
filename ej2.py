#n reinas back tracking
# numero de reinas
n = 6
# contador controla si encontro una solucion
contador = 0
columna = [False]*n
# las diagonales ayudan para saber si las reinas
# comparten diagonales por lo tanto se amenazan
diagonal_izquierda = [False]*(n*2)
diagonal_derecha = [False]*(n*2)
solucion = []


# función recursiva
def backtrack(y,n,contador):
    if (y==n):
        #retorna
        return contador + 1

    for x in range(n):
        global columna
        global diagonal_izquierda
        global diagonal_derecha
        