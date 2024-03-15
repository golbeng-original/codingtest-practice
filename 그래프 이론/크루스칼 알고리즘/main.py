'''
크루스칼 알고리즘
'''

def find_root_node(v, parent_table):
    
    if parent_table[v] != v:
        parent_table[v] = find_root_node(parent_table[v], parent_table)

    return parent_table[v]

def main(input:str):

    lines = input.splitlines()
    v, e = map(int, lines[0].split())

    vertex_info_container:list[tuple] = []
    parent_table:list[int] = [i for i in range(v)]

    for i in range(1, e + 1):
        src_v, dst_v, distance = map(int, lines[i].split())

        vertex_info_container.append((src_v-1, dst_v-1, distance))

    vertex_info_container.sort(key=lambda e : e[2])
    # 
    result_node = []
    for vertex_info in vertex_info_container:

        src_v, dst_v, distance = vertex_info

        src_root = find_root_node(src_v, parent_table)
        dst_root = find_root_node(dst_v, parent_table)

        if src_root == dst_root:
            continue

        # union 연산
        if src_root < dst_root:
            parent_table[dst_root] = src_root
        else:
            parent_table[src_root] = dst_root

        result_node.append((src_v, dst_v, distance))
    

    result = 0
    for _, _, distance in result_node:
        result += distance

    print(result)


if __name__ == '__main__':

    question = '''
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
'''
    question = question.strip()

    main(question)