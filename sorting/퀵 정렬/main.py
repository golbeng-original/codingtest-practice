
def quick_sort(array, start_idx:int, end_idx:int):

    if start_idx >= end_idx:
        return
    
    pivot = start_idx
    left = start_idx + 1
    right = end_idx

    while left <= right:

        while left <= end_idx and array[left] <= array[pivot]:
            left += 1

        while right > start_idx and array[right] >= array[pivot]:
            right -=1
        
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]


    quick_sort(array, start_idx, right - 1)
    quick_sort(array, right + 1 , end_idx)

def main():
    array = [7,5,9,0,3,1,6,2,4,8]

    quick_sort(array, 0, len(array) - 1)

    print(array)

if __name__ == '__main__':
    main()