
def sorting_data(arr):
    pointer = 0
    while pointer < len(arr):
        for i in range(pointer, len(arr)):
            if arr[pointer] > arr[i]:
                arr[i], arr[pointer] = arr[pointer], arr[i]
        pointer += 1
    return arr
