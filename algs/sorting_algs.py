"""Sorting methods"""
from random import randint


# Insertion Sort
def insertion_sort(A):
    # for each elem, starting at 2nd elem (1st is already sorted)
    for i in range(1, len(A)):
        # for elem to the left of this one
        for j in range(i - 1, -1, -1):

            # elem to left of current index > elem at current index
            if A[j] > A[j + 1]:
                # swap the elems
                A[j], A[j + 1] = A[j + 1], A[j]
            else:
                break
    return A


# Quick Sort
def quicksort(A):
    if len(A) <= 1:
        return A

    lower, equal, higher = [], [], []
    pivot = A[randint(0, len(A) - 1)]  # select a random pivot value

    # put values into the 3 lists based on comparison to pivot
    for i in A:
        if i < pivot:
            lower.append(i)
        elif i == pivot:
            equal.append(i)
        else:
            higher.append(i)

    return quicksort(lower) + equal + quicksort(higher)
