'''
숫자 카드 게임은 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한장을 뽑는 게임이다.
단, 게임의 룰을 지키며 카드를 뽑아야 하고 룰은 다음과 같다.

1. 숫자가 쓰인 카드들이 N X M 형태로 놓여 있다. 
   이떄 N은 행의 개수를 의미하며, M은 열의 개수를 의미한다.
2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
3. 그다음 선택도니 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.
4. 따라서 처음에 카드를 골라낼 행을 선택할 떄, 이후 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을
   고려하여 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다.

##
첫줄에 숫자 카드들이 놓인 행의 개수 N M이 공백을 기준으로 각각 자연수로 주어진다. 
'''

def main(input:str):
    
    lines = input.splitlines()
    n, m = map(int, lines[0].split())

    pick_number = -1
    for i in range(1, n+1):
        numbers = list(map(int, lines[i].split()))
        row_min_number = min(numbers)

        if row_min_number > pick_number:
            pick_number = row_min_number

    print(pick_number)

if __name__ == '__main__':
    
    input_1:str = '3 3\n3 1 2\n4 1 4\n2 2 2'
    input_2:str = '2 4\n7 3 1 8\n3 3 3 4'
    
    main(input_1)
