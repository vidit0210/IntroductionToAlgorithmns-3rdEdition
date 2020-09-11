def selection_sort(A):
    minimium = None
    for i in range(len(A)):
        minimum = A[i]
        for j in range(i + 1, len(A)):
            if A[j] < minimum:
                minimium = j
    A[i], A[minimium] = A[minimium], A[i]


A = [3, 7, 1, 2, 4, 5]
selection_sort(A)
print(A)
