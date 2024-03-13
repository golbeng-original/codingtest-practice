
import heapq


INF = int(1e9)

##
def advanced_dijkstra(input:str):

    '''
    최대 힙 자료 구조를 활요한 다익스트라 알고리즘 O(V * logE)의 시간 복잡도이다.
    '''

    lines = input.splitlines()
    v, e = map(int, lines[0].split())
    start_vertex = int(lines[1])

    paths:dict[int, list[tuple]] = {}
    for v in range(1, v+1):
        paths[v] = []

    for i in range(2, e+2):
        start_v, end_v, weight = map(int,lines[i].split())
        paths[start_v].append((end_v, weight))

    # 계산 시작
    visited:list[bool] = [False] * v
    result:list[int] = [INF] * v

    # 계산 시작
    visited:list[bool] = [False] * v
    result:list[int] = [INF] * v

    queue = []
    heapq.heappush(queue, (0, start_vertex))

    result[start_vertex - 1] = 0
    while queue:
        
        _, target_vertex = heapq.heappop(queue)
        if visited[target_vertex - 1]:
            continue

        current_wieght = result[target_vertex - 1]

        for next_vertex, next_weight in paths[target_vertex]:
            
            next_v_weight = current_wieght + next_weight

            if next_v_weight < result[next_vertex - 1]:
                heapq.heappush(queue, (next_v_weight, next_vertex))

                result[next_vertex - 1] = next_v_weight

        visited[target_vertex - 1] = True

    print(result)

###
###
def original_dijkstra(input:str):

    '''
    전통적인 다익스트라 알고리즘이다 O(V^2)의 시간 복잡도를 갖는다.
    '''

    lines = input.splitlines()
    v, e = map(int, lines[0].split())
    start_vertex = int(lines[1])

    paths:dict[int, list[tuple]] = {}
    for v in range(1, v+1):
        paths[v] = []

    for i in range(2, e+2):
        start_v, end_v, weight = map(int,lines[i].split())
        paths[start_v].append((end_v, weight))

    # 계산 시작
    visited:list[bool] = [False] * v
    result:list[int] = [INF] * v

    result[start_vertex - 1] = 0
    while True:
        
        current_wieght = result[start_vertex - 1]

        for next_v_info in paths[start_vertex]:
            
            next_v = next_v_info[0]
            next_v_weight = current_wieght + next_v_info[1]

            if next_v_weight < result[next_v - 1]:
                result[next_v - 1] = next_v_weight

        visited[start_vertex - 1] = True

        start_vertex = find_next_vertex(result, visited)
        if not start_vertex:
            break

    print(result)


def find_next_vertex(result:list[int], visited:list[int]):

    next_vertex = None
    smallest_weight = INF
    for idx, weight in enumerate(result):
        if visited[idx] == True:
            continue

        if weight < smallest_weight:
            next_vertex = idx + 1
        
    return next_vertex

if __name__ == '__main__':
    
    question = '''
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
'''

    question = question.strip()
    
    #original_dijkstra(question)
    advanced_dijkstra(question)