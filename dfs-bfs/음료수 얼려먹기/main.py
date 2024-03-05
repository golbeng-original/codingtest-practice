
'''
N x M 크기의 얼음 틀이 있다.
구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된. 
구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성 하시오.
다음의 4 x 5 얼음 틀 예시에서는 아이스크림이 총 3개 생성된다.

- 첫번째 줄에 얼음 틀의 세로 길이 N과 가로길이 M이 주어진다.
- 두 번째 줄부터 N + 1 번째 줄까지 얼음 틀의 형태가 주어진다.
- 이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1이다.

한번에 만들수 있는 아이스크림 개수를 출력한다.
'''

from collections import deque

def visit_drink_element(
        raw_data:list[list[int]],
        position:tuple,
        size:tuple,
        queue:deque,
        inner_visited:set
):
    
    if position in inner_visited:
        return

    x = position[0]
    y = position[1]

    if x < 0 or x >= size[0]:
        return
    
    if y < 0 or y >= size[1]:
        return 
    
    value = raw_data[y][x]
    if value == 1:
        return
    
    queue.append(position)
    inner_visited.add(position)

def find_drink(
        raw_data:list[list[int]], 
        start_position:tuple,
        size:tuple,
        visited:set,
):

    if start_position in visited:
        return False

    start_value = raw_data[start_position[1]][start_position[0]]
    if start_value == 1:
        return False

    queue = deque()
    inner_visited = set()

    queue.append(start_position)
    inner_visited.add(start_position)

    while queue:
        search_position = queue.popleft()

        # 아래
        visit_drink_element(
            raw_data,
            (search_position[0], search_position[1] + 1),
            size,
            queue,
            inner_visited
        )
        
        # 오른쪽
        visit_drink_element(
            raw_data,
            (search_position[0] + 1, search_position[1]),
            size,
            queue,
            inner_visited
        )

        # 위
        visit_drink_element(
            raw_data,
            (search_position[0], search_position[1] - 1),
            size,
            queue,
            inner_visited
        )

        # 왼쪽
        visit_drink_element(
            raw_data,
            (search_position[0] - 1, search_position[1]),
            size,
            queue,
            inner_visited
        )

    for v in inner_visited:
        visited.add(v)

    return True

def main(input:str):
    
    lines = input.splitlines()
    n, m = map(int, lines[0].split())

    data = [[0 for _ in range(m)] for _ in range(n)]

    for row_idx in range(n):

        col_values = lines[1 + row_idx]

        for col_idx in range(m):
            data[row_idx][col_idx] = int(col_values[col_idx])

    visited = set()

    find_count = 0
    for y in range(n):
        for x in range(m):

            start_position = (x, y)
            finded = find_drink(
                raw_data=data, 
                start_position=start_position,
                size=(m, n),
                visited=visited
            )

            find_count += 1 if finded == True else 0

    print(find_count)

if __name__ == '__main__':
    
    raw_data = '''
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
'''

    raw_data = raw_data.strip()

    main(input=raw_data)