
def main():

    array = [7, 5, 8, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

    count = [0] * (max(array) + 1)

    for i in array:
        count[i] += 1

    sorted_array = []
    for idx, value in enumerate(count):

        if value == 0:
            continue
        
        for _ in range(value):
            sorted_array.append(idx)

    print(sorted_array)

if __name__ == '__main__':
    main()