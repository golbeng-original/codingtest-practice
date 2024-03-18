'''
동물원에서 막 탈출한 원숭이 한 마리가 세상 구경을 하고 있다.
어느 날 원숭이는 ‘평화로운 마을’에 잠시 머물렀는데 마침 마을 사람들은 도로 공사 문제로 머리를 맞대고 회의 중이었다.

마을은 N개의 집과 그 집들을 연결하는 M개의 길로 이루어져 있다.
길은 어느 방향으로든지 다닐수 있는 편리한 길이다.
그리고 길마다 길을 유지하는데 드는 유지비가 있다.
마을의 이장은 마을을 2개의 분리된 마을로 분할할 계획을 세우고 있다. 
마을이 너무 커서 혼자서는 관리할 수 없기 때문이다.
마을을 분할할 때는 각 분리된 마을 안에 집들이 서로 연결되도록 분할해야 한다. 
각 분리된 마을 안에 있는 임의의 두 집 사이에 경로가 항상 존재해야 한다는 뜻이다.
마을 에는 집이 하나 이상 있어야 한다.
그렇게 마을의 이장은 계획을 세우다가 마을 안에 길이 너무 많다는 생각을 하게 되었다.

일단 분리된 두 마을 사이에 있는 길들은 필요가 없으므로 없앨 수 있다.
그리고 각 분리된 마을 안에서도 임의의 두 집 사이에 경로가 항상 존재하게 하면서 길을 더 없앨 수 있다.

마을의 이장은 위 조건을 만족하도록 길들을 모두 없애고 나머지 길의 유지비의 합을 최소로 하고 싶다.
이것을 구하는 프로그 램을 작성하시오.

입력 조건
• 첫째 줄에 집의 개수 N, 길의 개수 M이 주어진다. N은 2 이상 100,000 이하인 정수이고, M은 1 이상 1,000,000 이하인 정수이다.
• 그다음 줄부터 M줄에 걸쳐 길의 정보가 A, B, C 3개의 정수로 공백으로 구분되어 주어지는데 A번 집
과 B번 집을 연결하는 길의 유지비가 C (1 ≤ C ≤ 1,000 )라는 뜻이다.

출력 조건
• 첫째 줄에 길을 없애고 남은 유지비 합의 최솟값을 출력한다.

해법

신장트리를 만든 후 가장 비용이 큰 간선을 제거 해주면 된다.
결국 신장 트리 2개가 생성된다.
'''

def find_parent_table(v, parent_table:list[int]):

    if parent_table[v] != v:
        parent_table[v] = find_parent_table(parent_table[v], parent_table)

    return parent_table[v]

def main(input:str):
    
    lines = input.splitlines()

    v, e = map(int, lines[0].split())

    parent_table = [i for i in range(v)]

    vertex_distance_container = []
    for i in range(1 , e + 1):

        a, b, distance = map(int, lines[i].split())
        a = a - 1
        b = b - 1

        vertex_distance_container.append((a, b, distance))

    vertex_distance_container.sort(key=lambda e: e[2])

    result_nodes = []
    for vertex_distance_unit in vertex_distance_container:

        a, b, distance = vertex_distance_unit

        a_1 = find_parent_table(a, parent_table)
        b_1 = find_parent_table(b, parent_table)

        if a_1 == b_1:
            continue
        
        result_nodes.append((a, b, distance))

        if a_1 < b_1:
            parent_table[b_1] = a_1
        else:
            parent_table[a_1] = b_1

    result = 0
    max_distance = 0
    for _, _, distance in result_nodes:
        result += distance

        max_distance = max(max_distance, distance)

    print(result - max_distance)

if __name__ == '__main__':
    question = '''
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
'''
    question = question.strip()

    main(question)