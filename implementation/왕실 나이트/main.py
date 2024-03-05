'''
왕국의 정원은 체크판과 같은 8x8 좌표 평면이다. 황실 정원의 특정한 한 칸에 나이트가 서 있다.
나이트는 매우 충성스러운 신하로서 매일 무술을 연마한다.

나이트는 말을 타고 있기 떄문에 이동을 할 때는 L자 형태로만 이동할 수 있으며 정원 밖으로는 나갈 수 없다.
나이트는 특정한 위치에서 다음과 같은 2가지 경우로 이동할 수 있다.
1. 수평으로 두칸 이동한 뒤에 수직으로 한 칸 이동하기
2. 수직으로 두칸 이동한 뒤에 수평으로 한 칸 이동하기

  a b c d e f g h
1
2     
3
4
5
6
7
8

이처럼 8x8 좌표 평면상에서 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는
프로그램을 작성하시오.

예를 들어 만약 나이트가 a1에 있을 때 이동할 수 있는 경우의 수는 다음 2가지이다. 
a1의 위치는 좌표 평면에서 구석의 위치에 해당하며 나이트는 정원의 밖으로는 나갈 수 없기 때문이다.
1. 오른쪽으로 두 칸 이동 후 아래로 한 칸 이동하기( c2 ) 
2. 아래로 두 칸 이동 후 오른쪽으로 한 칸 이동하기( b3 )

또 다른 예로 나이트가 c2에 위치해 있다면 나이트가 이동할 수 있는 경우의 수는 6가지이다. 
이건 직접 계산해보시오.
'''

def main(input:str):

    moveable_elementes:list[tuple] = [
        (-1, -2),
        (1, -2),
        (-2, -1),
        (-2, 1),
        (2, -1),
        (2, 1),
        (-1, 2),
        (1, 2)
    ]
    
    col = input[0]
    col = int(ord(col) - ord('a')) + 1
    row = int(input[1])

    result = 0
    for moveable_element in moveable_elementes:

        nrow = row + moveable_element[0]
        ncol = col + moveable_element[1]

        if ncol < 1 or nrow < 1:
            continue

        if ncol > 8 or nrow > 8:
            continue

        result += 1

    print(result)

if __name__ == '__main__':

    question:str = 'a1'

    main(question)