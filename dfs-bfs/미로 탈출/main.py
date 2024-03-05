'''
동빈이는 N x M 크기의 직사각형 형태의 미로에 갇혀 있다.
미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 한다.
동빈이의 위치는 (1, 1)이고 미로의 출구는 (N, M)의 위치에 존재하며 한번에 한 칸씩 이동할 수 있다.
이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다. 
미로는 반드시 탈출할 수 있는 형태로 제시된다. 
이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오. 
칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.
'''

from collections import deque

def find_next_element(
        map_data:list[list[int]],
        next_position:tuple,
        queue:deque,
        visited_position:set,
        add_value:int
    ):
    
    if next_position in visited_position:
        return
    
    x = next_position[0]
    y = next_position[1]
    
    if x < 0 or x >= len(map_data[0]):
        return
    
    if y < 0 or y >= len(map_data):
        return

    map_value = map_data[y][x]
    if map_value == 0:
        return
    
    map_data[y][x] = map_value + add_value
    queue.append(next_position)
    visited_position.add(next_position)

def find_path(
        map_data:list[list[int]], 
        start_position:tuple,
        dest_position:tuple
    ):

    visited_position = set()
    
    queue = deque()
    queue.append(start_position)
    visited_position.add(start_position)

    result = -1
    while queue:
        
        position:tuple = queue.popleft()
        curr_value = map_data[position[1]][position[0]]

        # 위치 도달
        if position == dest_position:
            result = map_data[dest_position[1]][dest_position[0]]
            break

        # 위
        find_next_element(
            map_data,
            (position[0], position[1] - 1),
            queue,
            visited_position,
            curr_value
        )

        # 오른쪽
        find_next_element(
            map_data,
            (position[0] + 1, position[1]),
            queue,
            visited_position,
            curr_value
        )

        # 아래
        find_next_element(
            map_data,
            (position[0], position[1] + 1),
            queue,
            visited_position,
            curr_value
        )

        # 왼쪽
        find_next_element(
            map_data,
            (position[0] - 1, position[1]),
            queue,
            visited_position,
            curr_value
        )

    print(result)
        

def main(input:str):
    
    lines = input.splitlines()

    n, m = map(int, lines[0].split())

    map_data = [[0 for _ in range(m)] for _ in range(n)]

    for row_idx in range(n):
        for col_idx in range(m):
            map_data[row_idx][col_idx] = int(lines[1 + row_idx][col_idx])

    start_position = (0, 0)
    dest_position = (m - 1, n - 1)

    find_path(
        map_data,
        start_position,
        dest_position
    )


if __name__ == '__main__':

    question = '''
5 6
101010
111111
000001
111111
111111
'''

    question = question.strip()
    main(question)