# Run the sorting functions here

import random
import sorting_algs


# Return a list of size length - each elem is random int in range given
# Ex) random_list((1, 100), 5) -> A list of 5 random ints from 1 to 100
def random_list(length, span):
    the_list = []
    for i in range(length):
        the_list.append(random.randint(span[0], span[1]))
    return the_list


# Generate a random lists, sort them, and display the before/after

a_list = random_list((1, 100), 5)
print("Input list:\n" + str(a_list))
print("Insertion sort:\n" + str(sorting_algs.insertion_sort(a_list)))
