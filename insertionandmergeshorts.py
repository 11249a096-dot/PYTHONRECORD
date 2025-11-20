# ---------------------------------------
# Insertion Sort
# ---------------------------------------
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    
    return arr


# ---------------------------------------
# Merge Sort
# ---------------------------------------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split array into halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    sorted_list = []
    i = j = 0

    # Compare and merge
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Add remaining elements
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list


# ---------------------------------------
# Main Program
# ---------------------------------------
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]

    print("Original list:", arr)

    print("Insertion Sort:", insertion_sort(arr.copy()))
    print("Merge Sort:", merge_sort(arr.copy()))
