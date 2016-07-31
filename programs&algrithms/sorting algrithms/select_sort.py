



def select_sort(arr):
    sorted_idx = 0
    length = len(arr)

    while sorted_idx < length - 1:
        min_idx = minimun_idx(arr, sorted_idx)
        arr[sorted_idx], arr[min_idx] = arr[min_idx], arr[sorted_idx]
        sorted_idx += 1
    return arr


def minimun_idx(arr, start_idx):
    minimum = arr[start_idx]
    min_idx = start_idx
    length = len(arr)

    idx = start_idx
    while idx < length:
        if arr[idx] < minimum:
            minimum = arr[idx]
            min_idx = idx
        idx += 1

    return min_idx





