
INF = int(1e9)


def main(input:str):
    
    lines = input.splitlines()
    v = int(lines[0])
    e = int(lines[1])

    # 초기화
    graph = [[INF] * v for _ in range(v)]
    for i in range(2, e + 2):
        curr_v, next_v, distance = map(int, lines[i].split())
        graph[curr_v - 1][next_v - 1] = distance
        
    for i in range(v):
        graph[i][i] = 0 

    print(graph)

    # k 번째
    for k in range(v):
        
        # 계산 해야 할 경로 수집
        # D_ab = min(D_ab, D_ak + D_kb)
        for a in range(v):
            for b in range(v):
                # 거리 갱신
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
        
        #for a, b in pick_paths:
        #    prev_distance = result[a][b]
        #    lhs = graph[a][k]
        #    rhs = graph[k][b]
                
        #    result[a][b] = min(prev_distance, lhs + rhs)

    print(graph)


if __name__ == '__main__':

    question = '''
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
'''

    question = question.strip()

    main(question)