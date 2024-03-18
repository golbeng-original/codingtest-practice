'''
동빈이는 온라인으로 컴퓨터공학 강의를 듣고 있다.
이때 각 온라인 강의는 선수 강의가 있을 수 있는데,
선수 강의가 있는 강의는 선수 강의를 먼저 들어야만 해당 강의를 들을 수 있다. 

예를 들어 ‘알 고리즘’ 강의의 선수 강의로 ‘자료구조’와 ‘컴퓨터 기초’가 존재한다면, 
‘자료구조’와 ‘컴퓨터 기초’를 모두 들은 이후에 ‘알고리즘’ 강의를 들을 수 있다.
동빈이는 총 N개의 강의를 듣고자 한다. 
모든 강의는 1번부터 N번까지의 번호를 가진다. 
또한 동시에 여러 개의 강의를 들을 수 있다고 가정한다. 

예를 들어 N = 3일 때, 3번 강의의 선수 강의로 1번과 2번 강의가 있고, 1번과 2번 강의는 선수 강의가 없다고 가정하자. 
그리고 각 강의에 대하여 강의 시간이 다음과 같다고 가정하자.

- 1번 강의 : 30시간
- 2번 강의 : 20시간
- 3번 강의 : 40시간

이 경우 1번 강의를 수간하기까지의 최소 시간은 30시간, 2번 강의를 수강하기까지의 최소 시간은 20시간,
3번 강의를 수강하기까지의 최소 시간은 70시간이다.

동인이가 듣고자 하는 N개의 강의 정보가 주어졌을때,
N개의 강의에 대하여 수강하기까지 거리는 최소 시간을 각각 출력하는 프로그램을 작성하시오.

입력 조건
• 첫째 줄에 동빈이가 듣고자 하는 강의의 수 N (1 ≤ N ≤ 500 )이 주어진다.
• 다음 N개의 줄에는 각 강의의 강의 시간과 그 강의를 듣기 위해 먼저 들어야 하는 강의들의 번호가 자연수로 주어지며, 각 자연수는 공백으로 구분한다. 이때 강의 시간은 100,000 이하의 자연수이다.
• 각 강의 번호는 1부터 N까지로 구성되며, 각 줄은 -1로 끝난다.

출력 조건
• N개의 강의에 대하여 수강하기까지 걸리는 최소 시간을 한 줄에 하나씩 출력한다.
'''

class CurriculumInfo:

    def __init__(self):
        self.class_weight:int = 0
        self.prev_class:list[int] = []

        self.degree = 0 

        self.sum_weight:int = 0

    def add_prev_class(self, prev_class_num:int):
        self.prev_class.append(prev_class_num)
        self.degree += 1

    def sub_prev_class(self, prev_class_num:int, prev_weight:int):

        if prev_class_num in self.prev_class:
            self.prev_class.remove(prev_class_num)
            self.degree -= 1

            self.sum_weight += prev_weight

    @property
    def total_weight(self):
        return self.class_weight + self.sum_weight

    def __str__(self):
        return f'[weight: {self.class_weight}][next_class: {self.prev_class}][degree: {self.degree}]'

def find_zero_degree(graph_infos:list[CurriculumInfo]):

    zero_degree_class_index = []
    for idx, e in enumerate(graph_infos):
        if e.degree == 0:
            e.degree = -1
            zero_degree_class_index.append(idx)

    return zero_degree_class_index

def main(input:str):

    lines = input.splitlines()
    n = int(lines[0])

    graph_infos:list[CurriculumInfo] = []
    for i in range(n):
        graph_infos.append(CurriculumInfo())

    for i in range(1, n + 1):
        graph_raw_info = list(map(int, lines[i].split()))
        complete_time = graph_raw_info[0]

        graph_infos[i - 1].class_weight = complete_time

        graph_raw_info = graph_raw_info[1:]
        for prev_class_num in graph_raw_info:
            if prev_class_num == -1:
                break

            graph_infos[i - 1].add_prev_class(prev_class_num - 1) 

    # 계산 하기
    queue = []
    #result = [0] * n
    zero_degree_indices = find_zero_degree(
        graph_infos
    )

    #for idx in zero_degree_indices:
    #    graph_infos[idx].degree -= 1

    for e in zero_degree_indices:
        queue.append(e)

    while queue:
        
        check_idx = queue.pop(0)
        prev_weight = graph_infos[check_idx].total_weight

        for e in graph_infos:
            e.sub_prev_class(check_idx, prev_weight)

        zero_degree_indices = find_zero_degree(
            graph_infos
        )

        for e in zero_degree_indices:
            queue.append(e)

    for e in graph_infos:
        print(e.total_weight)

if __name__ == '__main__':
    
    question = '''
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
    '''

    question = question.strip()

    main(question)