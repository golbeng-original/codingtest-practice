'''
N명의 학생 정보가 있다.
학생 정보는 학생의 이름과 학생의 성적으로 구분된다. 
각 학생의 이름과 성적 정보가 주어졌을 때 성적이 
낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성하시오.
'''

def main(input:str):
    
    lines = input.splitlines()
    n = int(lines[0])

    students = []
    for i in range(1, n+1):
        name, score = lines[i].split()

        students.append((name, int(score)))

    for i in range(1, len(students)):

        for j in range(i, 0, -1):

            lhs_score = students[j-1]
            rhs_score = students[j]
            if lhs_score > rhs_score:
                students[j-1], students[j] = students[j], students[j-1]

    for student in students:
        print(student[0], end=' ')

if __name__ == '__main__':

    question = '''
2
홍길동 95
이순신 77
'''
    question = question.strip()

    main(question)