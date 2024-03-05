
def binary_search(
        array, 
        target_value:int, 
        start_idx:int, 
        end_idx:int
    ):

    if start_idx >= end_idx:
        return None

    mid_idx = (end_idx + start_idx) // 2
    if array[mid_idx] == target_value:
        return mid_idx
    
    elif target_value < array[mid_idx]:
        return binary_search(array, target_value, start_idx, mid_idx - 1)

    else:
        return binary_search(array, target_value, mid_idx + 1, end_idx)


def main():

    array = [0, 3, 5, 8, 10, 14, 22, 29, 33, 35, 40, 41, 44]

    find_idx = binary_search(
        array,
        35,
        0,
        len(array) - 1
    )

    print(find_idx)

if __name__ == '__main__':
    main()