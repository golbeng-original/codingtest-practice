'''
하나의 수열에는 다양한 수가 존재한다.
이러한 수는 크기에 상관없이 나열되어 있다. 
이 수를 큰 수부터 작은 수의 순서로 정렬해야 한다.
수열을 내림차순으로 정렬하는 프로그램을 만드시오.
'''


def main(input:str):
    
    array = list(map(int, input.splitlines()))
    print(array)

    for i in range(len(array) - 1):

        for j in range(i+1, len(array)):
            if array[i] < array[j]:
                array[i], array[j] = array[j], array[i]


    print(array)

if __name__ == '__main__':
    
    question = '''
3
15
27
12
'''
    question = question.strip()
    
    main(question)