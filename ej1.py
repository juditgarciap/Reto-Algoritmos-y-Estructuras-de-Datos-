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