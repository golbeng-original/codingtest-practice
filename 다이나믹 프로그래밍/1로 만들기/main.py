'''
정수 X가 주어질 때 정수 X에 사용할 수 있는 연산은 다음과 같이 4가지이다.
ⓐ X가 5로 나누어떨어지면, 5로 나눈다.
ⓑ X가 3으로 나누어떨어지면, 3으로 나눈다.
ⓒ X가 2로 나누어떨어지면, 2로 나눈다.
ⓓ X에서 1을 뺀다.

정수 X가 주어졌을 때, 연산 4개를 적절히 사용해서 1을 만들려고 한다.
연산을 사용하는 횟수의 최솟값을 출력하시오.

예를 들어 정수가 26이면 다음과 같이 계산해서 3번의 연산이 최솟값이다.
1. 26 - 1 = 25 (ⓓ)
2. 25 / 5 = 5 (ⓐ) 
3. 5 / 5 = 1 (ⓐ)
'''

# 핵심은 점화식을 만들 수 있는가이다..

# 메모제이션
dp = [0] * 300001
def dp_top_bottom_solution(value:int):
    
    '''
    탑-다운 메모제이션 방식
    '''

    if value == 1:
        return 0
    
    if dp[value] != 0:
        return dp[value]

    # a
    a_count = 9999999
    b_count = 9999999
    c_count = 9999999
    if value % 5 == 0:
        a_count = dp_top_bottom_solution(value // 5)

    # b
    if value % 3 == 0:
        b_count = dp_top_bottom_solution(value // 3)

    # c
    if value % 2 == 0:
        c_count = dp_top_bottom_solution(value // 2)

    # d
    d_count = dp_top_bottom_solution(value - 1)
    dp[value] = min(a_count, b_count, c_count, d_count) + 1

    return dp[value]


def dp_bottom_top_solution(value:int):
    
    '''
    바텀-업 방식
    '''

    for i in range(2, value + 1):

        dp[i] = dp[i-1] + 1

        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

        if i % 5 == 0:
            dp[i] = min(dp[i], dp[i // 5] + 1)

    return dp[value]

def main(input:str):
    
    value = int(input)

    #count = dp_top_bottom_solution(value)
    count = dp_bottom_top_solution(value)
    print(count)

if __name__ == '__main__':

    question = '26'

    main(question)