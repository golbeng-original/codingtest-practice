'''
어떤한 수 N이 1이 될 떄까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다.
단, 두 번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있다.

1. N에서 1을 뺀다.
2. N을 K로 나눈다.

예를 들어 N이 17, K가 4라고 가정하자. 이때 1번의 과정을 한번 수행하면 N은 16이 된다.
이후에 2번의 과정을 두번 수행하면 N은 1이 된다.
결과적으로 이 경우 전체 과정을 실행한 횟수는 3이 된다.
이는 N을 1로 만드는 최소 횟수 이다.
'''


def main(input:str):
    
    n, k = map(int, input.split())

    repeat_count = 0
    while True:
        
        # n이 k보다 작다면
        if n < k:
            remain_count = n - 1
            n = 1
            repeat_count = repeat_count + remain_count
            break

        # K의 배수가 될떄까지 빼기
        if n > k:
            remain_count = n % k
            repeat_count = repeat_count + remain_count
            n = n - remain_count

        # n/k 수행
        n = n // k
        repeat_count = repeat_count + 1

    print(repeat_count)

if __name__ == '__main__':
    
    input_1 = '25 5'
    input_2 = '25 3'
    main(input_2)