'''
정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에 3이 하나라도 포함되는
모든 경우의 수를 구하는 프로그램을 작성하시오.
예를 들어 1을 입력했을 때 다음은 3이 하나라도 포함되어 있으므로 세어야 하는 시각이다.

- 00시 00분 03초
- 00시 13분 30초

바면에 3이 하나라도 포함되어 있지 않으므로 세면 안되는 시각이다.
- 00시 02분 55초
- 00시 27분 45초

경우의 수가 100만개 이하이면 완전 탐색을 사용해도 괜찮다??
'''


def main(input:str):
    
    hour = int(input)

    result = 0
    for h in range(0, hour + 1):
        for m in range(0, 60):
            for s in range(0, 60):
                time = str(h) + str(m) + str(s)
                if '3' in time:
                    result += 1
    
    print(result)   

if __name__ == '__main__':
    
    question = '5'

    main(question)