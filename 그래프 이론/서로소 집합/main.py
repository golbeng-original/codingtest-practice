'''
서로소 집합 알고리즘 구현
'''

####################
def find_parent(element, parent_table:list[int]):

    # 다순 부모 찾기
    #if parent_table[element] != element:
    #    return find_parent(parent_table[element], parent_table)
    #return element
    #

    # 경로 압축 기법 - 재귀 적으로 찾고 최고 부모를 부모 테이블에 갱신
    if parent_table[element] != element:
        parent_table[element] = find_parent(parent_table[element], parent_table)
    return parent_table[element]

def union(union:tuple, parent_table:list[int]):

    x, y = union

    a = find_parent(x, parent_table)
    b = find_parent(y, parent_table)

    if a < b:
        parent_table[b] = a
    else:
        parent_table[a] = b
####################
        
# 서로소 집합 알고리즘
def make_mutually_exclusive():

    question = '''
6 4
1 4
2 3
2 4
5 6
'''
    question = question.strip()

    lines = question.splitlines()
    vertex, edge = map(int, lines[0].split())

    parent_table = [i for i in range(vertex)]

    ## 초기화
    unions = []
    for i in range(1, edge + 1):
        x, y = map(int, lines[i].split())
        unions.append((x - 1 , y - 1))

    ### find - union 과정
    for union_element in unions:
        union(union_element, parent_table)

    for i in range(vertex):

        root_vertex = find_parent(i, parent_table)
        print(root_vertex + 1, end=' ')

    print()

    for parent_element in parent_table:
        print(parent_element + 1, end=' ')


# 사이클 여부 판별
def check_circle_mutually_exclusive():

    question = '''
3 3
1 2
1 3
2 3
'''
    question = question.strip()

    lines = question.splitlines()
    vertex, edge = map(int, lines[0].split())

    parent_table = [i for i in range(vertex)]

    ## 초기화
    unions = []
    for i in range(1, edge + 1):
        x, y = map(int, lines[i].split())
        unions.append((x - 1 , y - 1))

    is_cycle = False
    for union_element in unions:

        x, y = union_element
        a = find_parent(x, parent_table)
        b = find_parent(y, parent_table)

        if a == b:
            is_cycle = True
            break

        union(union_element, parent_table)

    msg = 'Cycle 발생' if is_cycle else 'Cycle 없음'
    print(msg)

def main(input:str):

    #make_mutually_exclusive()
    check_circle_mutually_exclusive()

if __name__ == '__main__':
    
    question = '''
6 4
1 4
2 3
2 4
5 6
'''
    question = question.strip()
    
    main(question)