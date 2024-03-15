'''
위상정렬 알고리즘
'''

INF = int(1e9)

def find_zero_degree_node(degree_table:list[int]):

    find_indices = []
    for idx, degree in enumerate(degree_table):

        if degree == 0:
            find_indices.append(idx)
            degree_table[idx] -= 1

    return find_indices

def main(input:str):
    
    lines = input.splitlines()

    v, e = map(int, lines[0].split())

    degree_table = [0] * v

    graph = [[] for _ in range(v)]
    for i in range(1, e + 1):
        src_v, dst_v = map(int, lines[i].split())

        graph[src_v - 1].append(dst_v - 1)
        degree_table[dst_v - 1] += 1

    result_nodes = []
    queue = []
    find_nodes = find_zero_degree_node(degree_table)
    for node in find_nodes:
        queue.append(node)

    while queue:

        node = queue.pop(0)
        print(node+1)
        result_nodes.append(node)

        for next_node in graph[node]:
            degree_table[next_node] -= 1

        find_nodes = find_zero_degree_node(degree_table)
        for node in find_nodes:
            queue.append(node)

    result = ' - '.join(map(lambda e: f'{e+1}', result_nodes))
    print(result)

if __name__ == '__main__':
    
    question = '''
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
'''
    question = question.strip()
    
    main(question)