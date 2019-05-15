"""Sorting methods"""


# Insertion sort
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
