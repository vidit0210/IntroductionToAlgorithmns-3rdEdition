def selection_sort(A):
    for i in range(len(A)):
        minimum = A[i]
        for j in range(len(A)):
            if A[j] < minimum:
                A[i] = A[j]


A = [3, 7, 1, 2, 4, 5]
selection_sort(A)
print(A)
