# mapa de posibles pasos empezando por cada numero
NEIGHBORS_MAP = {
    1: (6, 8),
    2: (7, 9),
    3: (4, 8),
    4: (3, 9, 0),
    5: tuple(),  # 5 no tiene camino 
    6: (1, 7, 0),
    7: (2, 6),
    8: (1, 3),
    9: (2, 4),
    0: (4, 6),
}
def neighbors(position):
    # retorna cada numero a donde puede llegar
    return NEIGHBORS_MAP[position]

def yield_sequences(starting_position, num_hops, sequence=None):
    if sequence is None:
        # inicia la secuencia
        sequence = [starting_position]
        # cuando la función recursiva llega a numero de pasos 0
    # retorna la secuencia acumulada
    if num_hops == 0:
        yield sequence
        # como se usa generadores el return hace que salga definitivamente
        return

    # para la posición en la que inicia retorno los numeros a 
    # los que puede llegar y para cada numero ejecuto de nuevo
    # la función recursiva para saber a cuales puede llegar 
    # es necesario disminuir el numero de pasos para terminar la función
    # y cada numero al que es posible llegar (vecino) lo agrego a la secuencia
    for neighbor in neighbors(starting_position):
        # para saber un poco mas de yield from:https://es.stackoverflow.com/questions/313174/funcionamiento-de-yield-from
        yield from yield_sequences(
            neighbor, num_hops - 1, sequence + [neighbor])



def count_sequences(num_hops):
    num_sequences = 0
    # para cada posible numero de inicio se busca cuantos movimientos
    # son posibles de realizar
    # finalmente se cuentan cuantos movimientos por numero
    for posible_start_number in [1,2,3,4,5,6,7,8,9,0]:
        for sequence in yield_sequences(posible_start_number, num_hops):
            num_sequences += 1
    return num_sequences


# para completar la tabla
for n_hop in [1,2,3,5,8,10,15,18,21,23,32]:
    pos_val = count_sequences(num_hops=n_hop)
    print('Número de movimientos: {} --> posibilidades válidas: {}'.format(n_hop, pos_val))
    
#Número de movimientos: 1 --> posibilidades válidas: 20
#Número de movimientos: 2 --> posibilidades válidas: 46
#Número de movimientos: 3 --> posibilidades válidas: 104
#Número de movimientos: 5 --> posibilidades válidas: 544
#Número de movimientos: 8 --> posibilidades válidas: 6576
#Número de movimientos: 10 --> posibilidades válidas: 34432
#Número de movimientos: 15 --> posibilidades válidas: 2140672
#Número de movimientos: 18 --> posibilidades válidas: 25881088
#Número de movimientos: 21 --> posibilidades válidas: 307302400
#Número de movimientos: 23 --> posibilidades válidas: 1609056256 
