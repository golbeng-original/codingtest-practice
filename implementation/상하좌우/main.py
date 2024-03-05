'''

N X N 크기의 정사각형 공간에서 가장 왼쪽 위 좌표는 (1, 1) 이다
가장 오른쪽 아래 좌표는 (N, N)에 해당한다.

계획서에는 L,R,U,D 중 하나의 문자가 반복적으로 적혀있으며 각 문자의 의미는 다음과 같다
L : 왼쪽으로 한칸 이동
R : 오른쪽으로 한칸 이동
U : 위쪽으로 한칸이동
D : 아래쪽으로 한칸이동

N X N 크기의 정사각형을 공간을 벗어나는 움직임은 무시된다.
예를 들어 (1, 1)의 위치에서 L, U를 만나면 무시된다.

최종적으로 A가 도착하게 되는 좌표를 출력하면 된다.
'''

def main(input:str):

    lines = input.splitlines()
    n = int(lines[0])

    move_units = lines[1].split()

    x = 1
    y = 1

    for move_unit in move_units:
        
        if move_unit == 'L':
            y = y - 1 if y - 1 > 1 else y 
            
        if move_unit == 'R':
            y = y + 1 if y + 1 <= n else y

        if move_unit == 'U':
            x = x - 1 if x - 1 > 1 else x

        if move_unit == 'D':
            x = x + 1 if x + 1 <= n else x

    print(f'({x}, {y})')
    

if __name__ == '__main__':

    question = '5\nR R R U D D'

    main(question)