# -- Titulo x 2 Segundos --

# -- Mostrar hook antes de transición --
# Hasta ahora.. Denada... Presta atencion... Te arrepentiras si no lo guardas..

# -- Content items -- 
# Tip / Info
# Description

# -- Outro & CTA --
# Save the video / Comment "Word"

##---------------------------------------------------------------------------
import random

def shuffle_data(data):
    shuffled_data = data
    random.shuffle(shuffled_data)
    return shuffled_data

data = {
  "tips": [
    "tip 2",
    "tip 1",
    "tip 3",
    "tip 7",
    "tip 4",
    "tip 5",
    "tip 6",
  ],
}

def deck(data):
    index_count = {}

    # shuffled_data = shuffle_data(data)
    shuffled_data = data
    print("-----------------------------")
    print(shuffled_data)
    print("-----------------------------")

    # First iteration
    print (f"INDEX [0] | Resultado {shuffled_data[0]}")
    print (f"INDEX [1] | Resultado {shuffled_data[1]}")
    print (f"INDEX [2] | Resultado {shuffled_data[2]}")

    first_index = 0
    third_index = 2

    for i in range(len(shuffled_data)):
        index_count[f"{i + 1 }"] = 0
        
 
    print("-----------------------------")
    print(index_count)

    for i in range(3):
        new_first_index = (third_index + 1) % len(shuffled_data)  # Utilizamos % para volver al inicio si nos pasamos
        print (f"INDEX [{new_first_index}] | Resultado {shuffled_data[new_first_index]}")
        
        # index_count[str(new_first_index)] = index_count.get(str(new_first_index), 0) + 1 

        print (f"INDEX [{first_index}] | Resultado {shuffled_data[first_index]}")
        third_index = (new_first_index + 1) % len(shuffled_data)  # Utilizamos % para volver al inicio si nos pasamos
        print (f"INDEX [{third_index}] | Resultado {shuffled_data[third_index]}")

        first_index = (first_index + 1) % len(shuffled_data)  # Utilizamos % para volver al inicio si nos pasamos
        print("-----------------------------")
    print(index_count)

print (deck(data['tips']))