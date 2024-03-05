'''
현민이는 게임 캐릭터가 맵 안에서 움직이는 시스템을 개발 중이다.
캐릭터가 있는 장소는 1 x 1 크기의 정사각형으로 이뤄진 N x M 크기의 직사각형으로, 각각의 칸은 육지 또는 바다이다.
캐릭 터는 동서남북 중 한 곳을 바라본다.
맵의 각 칸은 (A, B)로 나타낼 수 있고, 
A는 북쪽으로부터 떨어진 칸의 개수, B는 서쪽으로부터 떨어진 칸의 개수이다. 
캐릭터는 상하좌우로 움직일 수 있고, 바다로 되어 있는 공간에는 갈 수 없다.

캐릭터의 움직임을 설정하기 위해 정해 놓은 매뉴얼은 이러하다.
1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전한 방향)부터 차례대로 갈 곳을 정한다.
2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 
   왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진한다. 
   왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다.
   단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로갈 수 없는 경우에는 움직임을 멈춘다.

현민이는 위 과정을 반복적으로 수행하면서 캐릭터의 움직임에 이상이 있는지 테스트하려고 한다.
매뉴얼에 따라 캐릭터를 이동시킨 뒤에, 캐릭터가 방문한 칸의 수를 출력하는 프로그램을 만드시오.

첫째줄, 세로 크기 N, 가로 크기 M
둘째줄, 칸의 좌표 (A, B)와 바라보는 방향 d가 공백으로 구분하여 주어진다.
d의 값으로는 4가지 존대
- 0 : 북쪽
- 1 : 동쪽
- 2 : 남쪽
- 3 : 서쪽
셋째줄부터 맵인지 육지인지 대한 정보가 주어진다.
- 0 : 육지
- 1 : 바다
'''

class GameInfo:

    def __init__(self, raw_data:str):

        raw_data = raw_data.strip()
        lines = raw_data.splitlines()

        n, m = map(int, lines[0].split())
        self.a, self.b, self.d = map(int, lines[1].split())
        
        self.n = n
        self.m = m
        self.map_data = [[0 for col in range(m)] for row in range(n)]

        for y in range(m):
            row = list(map(int, lines[2+y].split()))

            for x in range(n):
                self.map_data[y][x] = row[x]


    def is_enable_move(self, next_step:tuple[int, int]):

        # 범위에 있나?
        if next_step[0] < 0 or next_step[0] >= self.n:
            return False
        
        if next_step[1] < 0 or next_step[1] >= self.m:
            return False
        
        return True
    
    def is_sea(self, next_step:tuple[int, int]):

        map_satus = self.map_data[next_step[1]][next_step[0]]
        if map_satus == 1:
            return True
        
        return False 


def main(input:str):
    
    gameinfo:GameInfo = GameInfo(input)
    print(gameinfo.map_data)

    # (x, y)
    direction_steps:list[tuple] = [
        (0, -1),
        (1, 0),
        (0, 1),
        (-1, 0)
    ]

    visit_history:set[tuple] = set()

    result = 1
    curr_x = gameinfo.b
    curr_y = gameinfo.a
    curr_d = gameinfo.d

    # 놓여진 위치를 history에 등록
    visit_history.add((curr_x, curr_y))

    while True:

        #print(f'x = {curr_x}, y = {curr_y}, d = {curr_d}')

        # 4방향 이동
        next_d = curr_d
        is_moved = False
        for i in range(4):
            
            # 왼쪽으로 회전

            next_d = next_d - 1 if next_d - 1 > 0 else 3
            next_direction_step = direction_steps[next_d]

            next_x = curr_x + next_direction_step[0]
            next_y = curr_y + next_direction_step[1]

            # 범위에 있나?
            if gameinfo.is_enable_move((next_x, next_y)) == False:
                continue

            # 다음 이동하게 될 좌표 및 맵 상태
            next_position = (next_x, next_y)

            # 가봤던 곳이나 바다이면
            if next_position in visit_history or \
                gameinfo.is_sea((next_x, next_y)) == True:
                continue
            
            # 방문 위치 저장
            visit_history.add(next_position)

            # 칸 이동
            curr_x = next_x
            curr_y = next_y
            curr_d = next_d
            is_moved = True
            result += 1
            break

        # 이동했다면 무시
        if is_moved == True:
            continue

        # 현재 보는 방향에서 뒤로 이동
        next_direction_step = direction_steps[curr_d]
        backward_direction_step = (
            next_direction_step[0] * -1,
            next_direction_step[1] * -1
        )
        
        # 뒤로 이동해야 하는 칸이 바다이면 종료
        if gameinfo.is_enable_move(backward_direction_step) == False or \
            gameinfo.is_sea(backward_direction_step) == True:
            break
        
        curr_x += next_direction_step[0]
        curr_y += next_direction_step[1]

    print(result)

if __name__ == '__main__':

    question = '''
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
'''

    main(question)