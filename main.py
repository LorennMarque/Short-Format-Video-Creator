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
    shuffled_data = data["tips"]
    random.shuffle(shuffled_data)
    return shuffled_data

import random

def shuffle_data(data):
    shuffled_data = data["tips"].copy()
    random.shuffle(shuffled_data)
    return shuffled_data

def create_f_deck(shuffled_data):
    f_deck = {}
    data_length = len(shuffled_data)
    first_index = 0
    last_index = 2
    used_items = set()

    f_deck["Block 1"] = [
        shuffled_data[0],
        shuffled_data[1],
        shuffled_data[2]
    ]
    used_items.update(f_deck["Block 1"])

    for i in range(3):
        first = (last_index + 1) % data_length
        second = (first_index + 1) % data_length
        third = (last_index + 2) % data_length

        new_block = [
            shuffled_data[first],
            shuffled_data[second],
            shuffled_data[third]
        ]

        # Check if at least 50% of the items in the new block are new
        new_items_count = sum(1 for item in new_block if item not in used_items)
        if new_items_count >= 2:
            f_deck["Block " + str(i+2)] = new_block
            used_items.update(new_block)
        else:
            # If not, shuffle the data again and try creating the block
            random.shuffle(shuffled_data)
            return create_f_deck(shuffled_data)

        first_index = second
        last_index = third

    return f_deck

data = {
  "tips": [
    "tip 1",
    "tip 2",
    "tip 3",
    "tip 4",
    "tip 5",
    "tip 6",
    "tip 7"
  ],
}

shuffled_data = shuffle_data(data)
f_deck = create_f_deck(shuffled_data)
print(f_deck)

