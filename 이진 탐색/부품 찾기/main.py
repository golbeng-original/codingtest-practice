'''
동빈이네 전자 매장에는 부품이 N개 있다. 
각 부품은 정수 형태의 고유한 번호가 있다. 
어느 날 손님이 M개 종류의 부품을 대량으로 구매하겠다며 당일 날 견적서를 요청했다.
동빈이는 때를 놓치지 않고 손님이 문의한 부품 M개 종류를 모두 확인해서 견적서를 작성해야 한다.
이때 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성해보자.
예를 들어 가게의 부품이 총 5개일 때 부품 번호가 다음과 같다고 하자.

N = 5
[ 8 , 3 , 7 , 9 , 2 ]

손님은 총 3개의 부품이 있는지 확인 요청했는데 부품 번호는 다음과 같다.

M = 3
[ 5 , 7 , 9 ]

이때 손님이 요청한 부품 번호의 순서대로 부품을 확인해 부품이 있으면 yes를,
없으면 no를 출력 한다. 구분은 공백으로 한다.
'''

def find_part(array, target_value):

    start_idx = 0
    end_idx = len(array) - 1

    while start_idx <= end_idx:

        mid_idx = (start_idx + end_idx) // 2
        if array[mid_idx] == target_value:
            return mid_idx
        
        elif target_value < array[mid_idx]:
            end_idx = mid_idx - 1

        else:
            start_idx = mid_idx + 1

    return None

def binarysearch_solution(
        n:int,
        n_array:list[int],
        m:int,
        m_array:list[int]
):
    '''
    이진 탐색 해법
    '''

    n_array.sort()

    for m_value in m_array:
        find_index = find_part(n_array, m_value)
        if find_index:
            print('yes', end=' ')
        else:
            print('no', end=' ')

def collection_solution(
        n:int,
        n_array:list[int],
        m:int,
        m_array:list[int]
):
    '''
    set 자료구조를 활용한 해법
    '''
    
    n_set = set(n_array)

    for m_value in m_array:

        if m_value in n_set:
            print('yes', end = ' ')
        else:
            print('no', end=' ')

def main(input:str):
    
    lines = input.splitlines()
    n = int(lines[0])
    n_array = list(map(int, lines[1].split()))

    m = int(lines[2])
    m_array = list(map(int, lines[3].split()))

    #binarysearch_solution(n, n_array, m, m_array)
    collection_solution(n, n_array, m, m_array)

if __name__ == '__main__':

    question = '''
5
8 3 7 9 2
3
5 7 9
'''

    question = question.strip()

    main(question)