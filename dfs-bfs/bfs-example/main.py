from collections import deque

def bfs_search(graph:list[list[int]], v:int):

    visited = [False] * 9

    queue = deque()

    visited[v] = True
    queue.append(v)

    while len(queue):

        search_value = queue.popleft()
        print(search_value, end=' ')

        for i in graph[search_value]:
            
            if visited[i]:
                continue
            
            visited[i] = True
            queue.append(i)

def main():

    graph = [
        [],
        [2, 3, 8],
        [1, 7],
        [1, 4, 5],
        [3, 5],
        [3, 4],
        [7],
        [2, 6, 8],
        [1, 7]
    ]

    bfs_search(graph=graph, v=1)

if __name__ == '__main__':
    main()