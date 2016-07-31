def quicksort(dataset):

    def _quicksort(sort, data):
        left, pivot, right = pivot_sort(data)

        if len(left) != 0:
            _quicksort(sort, left)

        sort.append(pivot)

        if len(right) != 0:
            _quicksort(sort, right)

    sort = []
    _quicksort(sort, dataset)

    return sort





def pivot_sort(arr):
    pivot = arr[0]
    left = []
    right = []

    for x in arr[1:]:
        if x < pivot:
            left.append(x)
        else:
            right.append(x)

    return  (left, pivot, right)





def assertion(actualAnswer, expectedAnswer):
    print("Your answer:    " + str(actualAnswer))
    print("Expcted answer: " + str(expectedAnswer))
    print(actualAnswer == expectedAnswer)

assertion(quicksort([4, 2, 5, 8, 6]), [2, 4, 5, 6, 8])
