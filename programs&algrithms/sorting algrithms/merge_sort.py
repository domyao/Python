def merge_sort(arr):
    sorted_arrs = list([x] for x in arr)

    while len(sorted_arrs) > 1:
        sorted_arrs.append( merge_two(sorted_arrs.pop(0),sorted_arrs.pop(0) ) )  # sorted_arrs keeping being changed
    return sorted_arrs[0]

    #------------------- or do it this way -----------------------
    # while len(sorted_arrs) > 1:
    #     merged = merge_two( sorted_arrs.pop(0),sorted_arrs.pop(0) )
    #     sorted_arrs.append(merged)
    # return merged
    # -------------------------------------------------------------



def merge_two(arr_l, arr_r):
    merged = []

    idx_l = 0
    idx_r = 0

    while idx_l < len(arr_l) and idx_r < len(arr_r):
        if arr_l[idx_l] <= arr_r[idx_r]:
            merged.append(arr_l[idx_l])
            idx_l += 1
        else:
            merged.append(arr_r[idx_r])
            idx_r += 1
    else:
        if idx_l == len(arr_l):  #left array reach its end
            merged.extend(arr_r[idx_r:])
        else:                    #idx_r == len(arr_r)   right array reached its end
            merged.extend(arr_l[idx_l:])

    return merged



if __name__ == "__main__":
    arr = [98, 744, 28, 81, 447, 2, 5, 10, 99, 55]
