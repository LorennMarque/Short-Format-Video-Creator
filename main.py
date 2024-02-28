# -- Titulo x 2 Segundos --

# -- Mostrar hook antes de transición --
# Hasta ahora.. Denada... Presta atencion... Te arrepentiras si no lo guardas..

# -- Content items -- 
# Tip / Info
# Description

# -- Outro & CTA --
# Save the video / Comment "Word"

import itertools
import random

def deck(data, group_size, max_repetitions):
    tips = data["tips"]
    num_tips = len(tips)

    # Generar todas las posibles combinaciones de tips de tamaño group_size
    combinations = list(itertools.combinations(tips, group_size))

    valid_combinations = []
    tip_counts = {tip: 0 for tip in tips}  # Contador para llevar el seguimiento de las repeticiones de cada tip en cada bloque

    # Mezclar el orden de las combinaciones para una distribución aleatoria
    random.shuffle(combinations)

    # Verificar cada combinación
    for combination in combinations:
        # Verificar si la combinación cumple con las restricciones de repeticiones en el bloque actual
        if all(tip_counts[tip] + combination.count(tip) <= max_repetitions for tip in set(combination)):
            # Mezclar el orden de los tips dentro de la combinación
            shuffled_combination = list(combination)
            random.shuffle(shuffled_combination)
            valid_combinations.append(shuffled_combination)
            # Incrementar el contador para los tips en esta combinación
            for tip in combination:
                tip_counts[tip] += combination.count(tip)

    return valid_combinations

data = {
  "tips": [
    "tip 1",
    "tip 2",
    "tip 3",
    "tip 4",
    "tip 5",
    "tip 6",
    "tip 7",
    "tip 8",
    "tip 9",
    "tip 10",
    "tip 11",
    "tip 12",
    "tip 13",
    "tip 14",
    "tip 15",
    "tip 16",
  ],
}

group_size = 3
max_repetitions = 3
print(deck(data, group_size, max_repetitions))

