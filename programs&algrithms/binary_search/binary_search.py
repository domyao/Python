
def binary_search(arr, tar):
    start = 0
    end = len(arr) - 1

    while end - start >= 0:
        mid_idx = (end - start) // 2 + start
        if tar < arr[mid_idx]:
            end = mid_idx - 1
        elif tar > arr[mid_idx]:
            start = mid_idx + 1
        else:
            return mid_idx

    return -1




if __name__ == "__main__":
    ##sample dataset
    arr = [1,3,9,11,23,44,66,88,102,142,188,192,239,382,492,1120,1900,2500,4392,5854,6543,8292,9999,29122]

    for idx, item in enumerate(arr):
        assert binary_search(arr, item) == idx, "failed"

    with open("wordlist.txt") as nf:
        words = nf.read().splitlines()

    assert words[binary_search(words, 'illuminatingly')] == 'illuminatingly', "failed"
    assert words[binary_search(words, 'lexicalisation')] == 'lexicalisation', "failed"
    assert words[binary_search(words, 'unexpectedness')] == 'unexpectedness', "failed"
