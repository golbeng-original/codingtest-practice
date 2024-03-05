'''
동빈이는 두 개의 배열 A와 B를 가지고 있다. 
두 배열은 N개의 원소로 구성되어 있으며, 배열의 원소는 모두 자연수이다. 
동빈이는 최대 K번의 바꿔치기 연산을 수행할 수 있는데, 
바꿔치기 연산이란 배열 A에 있는 원소 하나와 배열 B에 있는 원소 하나를 골라서 두 원소를 서로 바꾸는 것을 말한다.
동빈이의 최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것이며,
여러분은 동빈이를 도와야 한다.
N, K, 그리고 배열 A와 B의 정보가 주어졌을 때, 
최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력하는 프로그램을 작성하시오.
예를 들어 N = 5, K = 3이고 배열 A와 B가 다음과 같다고 하자.

•배열 A = [1, 2, 5, 4, 3] 
•배열 B = [5, 5, 6, 6, 5]

이 경우, 다음과 같이 세 번의 연산을 수행할 수 있다.

•연산 1 ) 배열 A의 원소 ‘1’과 배열 B의 원소 ‘6’을 바꾸기
•연산 2 ) 배열 A의 원소 ‘2’와 배열 B의 원소 ‘6’을 바꾸기
•연산 3 ) 배열 A의 원소 ‘3’과 배열 B의 원소 ‘5’를 바꾸기

세 번의 연산 이후 배열 A와 배열 B의 상태는 다음과 같이 구성될 것이다.

•배열 A = [6, 6, 5, 4, 5] 
•배열 B = [3, 5, 1, 2, 5]

이때 배열 A의 모든 원소의 합은 26이 되며, 이보다 더 합을 크게 만들 수는 없다.
따라서 이 예시의 정답은 26이 된다.

'''

def main(input:str):
    
    lines = input.splitlines()
    n, k = map(int, lines[0].split())

    array_1 = list(map(int, lines[1].split()))
    array_2 = list(map(int, lines[2].split()))

    array_1.sort()
    array_2.sort(reverse=True)

    for i in range(k):
        
        if array_1[i] < array_2[i]:
            array_1[i], array_2[i] = array_2[i], array_1[i]
            
        else:
            break

    result = sum(array_1)
    print(result)

if __name__ == '__main__':

    question = '''
5 3
1 2 5 4 3
5 5 6 6 5
'''
    question = question.strip()

    main(question)