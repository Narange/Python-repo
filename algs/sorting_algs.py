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


# Merge helper function
def merge(a, b):
    result = []
    index_a, index_b = 0, 0

    # while both lists are not yet empty, append the lesser element
    while(index_a < len(a) and index_b < len(b)):
        if(a[index_a] < b[index_b]):
            result.append(a[index_a])
            index_a += 1
        else:
            result.append(b[index_b])
            index_b += 1
        print(result)

    # one of the lists is empty; append the rest of the other
    if(index_a == len(a)):
        result.extend(b[index_b:])
    else:
        result.extend(a[index_a:])

    return result


# Merge Sort
def merge_sort(A):
    if len(A) <= 1:
        return A

    lower, higher = merge_sort(A[:len(A) / 2]), merge_sort(A[len(A) / 2:])
    return merge(lower, higher)
