

def insertion_sort(arr):

    sorted_idx = 0
    length = len(arr)

    while sorted_idx < length - 1:

        curr_idx = sorted_idx + 1
        while curr_idx > 0 and arr[curr_idx - 1] > arr[curr_idx]:
            arr[curr_idx - 1], arr[curr_idx] = arr[curr_idx], arr[curr_idx - 1]
            curr_idx -= 1

        sorted_idx += 1

    return arr



arr = [5,19,4,1,36,99,2]

# assert insertion_sort([5,19,4,1,36,99,2]) == sorted([5,19,4,1,36,99,2])
# assert insertion_sort(["Greg", "Armen", "Ken"]) == sorted(["Greg", "Armen", "Ken"])
# assert insertion_sort([9,8,7,6,5,4,3,2,1]) == [1,2,3,4,5,6,7,8,9]



















