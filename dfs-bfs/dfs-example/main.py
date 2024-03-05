

def dfs_search_entry(graph:list[list[int]], v:int):

    visited = [False] * 9
    dfs_search_recusive(graph=graph, v=v, visited=visited)

def dfs_search_recusive(graph:list[list[int]], v:int, visited:list[bool]):

    '''
    재귀 방식
    '''
    print(v, end=' ')
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs_search_recusive(graph=graph, v=i, visited=visited)    


def dfs_search_stack(graph:list[list[int]], v:int):

    '''
    스택 방식
    '''

    stack = []
    visited = [False] * 9
    
    stack.append(v)
    visited[v] = True
    print(v, end=' ')

    # stack이 비워질 때 까지
    while len(stack):

        is_append_stack = False
        for i in graph[stack[len(stack) - 1]]:

            if visited[i]:
                continue

            visited[i] = True
            stack.append(i)
            print(i, end=' ')
            is_append_stack = True
            break
        
        if is_append_stack == True:
            continue
    
        stack.pop()   


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

    #dfs_search_entry(graph=graph, v=1, visited=visited)
    dfs_search_stack(graph=graph, v=1)

if __name__ == '__main__':
    main()