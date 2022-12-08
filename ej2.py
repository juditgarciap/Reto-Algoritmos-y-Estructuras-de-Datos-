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
 # la primera diagonal es la diagonal normal
 # y la segunda es la invertida
        if(columna[x] or diagonal_izquierda[x+y] or diagonal_derecha[x-y+n-1]):
            continue
         # se coloca la reina
        columna[x] = diagonal_izquierda[x+y] = diagonal_derecha[x-y+n-1] = True
        solucion.append((x,y))

        # se envia la fila siguiente
        contador = backtrack(y+1,n,contador)

        # quiere decir que ya encontró una solución , si se quita esto encuentra todas
        if contador!=0:
            return contador

        # se quita la reina para probar otras posibilidades
        columna[x] = diagonal_izquierda[x+y] = diagonal_derecha[x-y+n-1] = False
        solucion.pop(-1)
    return contador

