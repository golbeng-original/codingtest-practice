'''
방문 판매원 A는 많은 회사가 모여 있는 공중 미래 도시에 있다.
공중 미래 도시에는 1번부터 N번 까지의 회사가 있는데 특정 회사끼리는 서로 도로를 통해 연결되어 있다.
방문 판매원 A는 현재 1번 회사에 위치해 있으며, X번 회사에 방문해 물건을 판매하고자 한다.

공중 미래 도시에서 특정 회사에 도착하기 위한 방법은 회사끼리 연결되어 있는 도로를 이용하는 방법이 유일하다.
또한 연결된 2개의 회사는 양방향으로 이동할 수 있다. 
공중 미래 도시에서의 도로는 마하의 속도로 사람을 이동시켜주기 때문에 특정 회사와 다른 회사가 도로로 연결되어 있다면,
 정확히 1만큼의 시간으로 이동할 수 있다.
또한 오늘 방문 판매원 A는 기대하던 소개팅에도 참석하고자 한다. 
소개팅의 상대는 K번 회사에 존재한다. 방문 판매원 A는 X번 회사에 가서 물건을 판매하기 전에 먼저 소개팅 상대의 회사에 찾아 가서 함께 커피를 마실 예정이다. 
따라서 방문 판매원 A는 1번 회사에서 출발하여 K번 회사를 방문한 뒤에 X번 회사로 가는 것이 목표다. 
이때 방문 판매원 A는 가능한 한 빠르게 이동하고자 한다.
방문 판매원이 회사 사이를 이동하게 되는 최소 시간을 계산하는 프로그램을 작성하시오. 
이때 소개 팅의 상대방과 커피를 마시는 시간 등은 고려하지 않는다고 가정한다. 

예를 들어 N = 5, X = 4, K = 5이고 회사 간 도로가 7개면서 각 도로가 다음과 같이 연결되어 있을 때를 가정할 수 있다.
(1번, 2번), (1번, 3번), (1번, 4번), (2번, 4번), (3번, 4번), (3번, 5번), (4번, 5번)

이때 방문 판매원 A가 최종적으로 4번 회사에 가는 경로를 (1번 - 3번 - 5번 - 4번)으로 설정하면,
소개팅에도 참석할 수 있으면서 총 3만큼의 시간으로 이동할 수 있다. 따라서 이 경우 최소 이동 시간은 3이다.

입력 조건
• 첫째 줄에 전체 회사의 개수 N과 경로의 개수 M이 공백으로 구분되어 차례대로 주어진다.
(1 ≤ N, M ≤ 100 )
• 둘째 줄부터 M + 1번째 줄에는 연결된 두 회사의 번호가 공백으로 구분되어 주어진다.
• M + 2번째 줄에는 X와 K가 공백으로 구분되어 차례대로 주어진다. (1 ≤ K ≤ 100 )

출력조건
• 첫째 줄에 방문 판매원 A가 K번 회사를 거쳐 X번 회사로 가는 최소 이동 시간을 출력한다.
• 만약 X번 회사에 도달할 수 없다면 -1을 출력한다.
'''

'''
해당 문제는 프로링드 워셜 알고리즘으로 풀어햐 한다!!
'''

INF = int(1e9)

def dijkstra(
        graph:list[list[int]],
        start_v:int,
        dest_v:int,
        #visited:list[bool]
    ):

    result = [INF] * len(graph)
    visited:list[bool] = [False] * len(graph)

    result[start_v] = 0

    while True:

        for next_v in graph[start_v]:

            next_distance = result[start_v] + 1

            if next_distance < result[next_v]:
                result[next_v] = next_distance

        visited[start_v] = True

        # 다음 노드 찾기
        start_v = -1
        check_distance = INF
        for idx, distance in enumerate(result):

            if visited[idx]:
                continue

            if distance < check_distance:
                start_v = idx
                check_distance = distance

        if start_v == -1:
            break

    return result[dest_v]

def floyd_warshal(
        graph:list[list[int]],
        path:list[int]
    ):

    v_count = len(graph)

    for k in range(v_count):

        for a in range(v_count):

            for b in range(v_count):

                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    # a -> k -> x
    a = path[0]
    k = path[1]
    x = path[2]
    distance = graph[a][k]
    distance += graph[k][x]

    if distance >= INF:
        print(-1)
        return

    print(distance)

def main(input:str):
    
    lines = input.splitlines()
    v, e = map(int, lines[0].split())
    x, k = map(int, lines[1 + e].split())

    graph = [[INF] * v for _ in range(v)]
    for i in range(1, 1 + e):
        start_v, end_v = map(int, lines[i].split())

        graph[start_v - 1][end_v - 1] = 1
        graph[end_v - 1][start_v - 1] = 1
    
    for i in range(v):
        graph[i][i] = 0

    floyd_warshal(graph, [0, k-1, x-1])

    '''
    k_distance = dijkstra(
        graph=graph,
        start_v=0,
        dest_v=k-1
    )

    x_distance = dijkstra(
        graph=graph,
        start_v=k-1,
        dest_v=x-1
    )

    result_distance = k_distance + x_distance
    if result_distance >= INF:
        print(-1)
        return

    print(result_distance)
    '''

if __name__ == '__main__':
    
    question = '''
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
'''

#    question = '''
#4 2
#1 3
#2 4
#3 4
#'''

    question = question.strip()

    main(question)