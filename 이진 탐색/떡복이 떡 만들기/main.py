'''
오늘 동빈이는 여행 가신 부모님을 대신해서 떡집 일을 하기로 했다.
오늘은 떡볶이 떡을 만드는 날이다.
동빈이네 떡볶이 떡은 재밌게도 떡볶이 떡의 길이가 일정하지 않다. 
대신에 한 봉지 안에 들어 가는 떡의 총 길이는 절단기로 잘라서 맞춰준다.
절단기에 높이(H)를 지정하면 줄지어진 떡을 한 번에 절단한다. 
높이가 H보다 긴 떡은 H 위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않는다.
예를 들어 높이가 19, 14, 10, 17cm인 떡이 나란히 있고 절단기 높이를 
15cm로 지정하면 자른 뒤떡의 높이는 15, 14, 10, 15cm가 될 것이다. 
잘린 떡의 길이는 차례대로 4, 0, 0, 2cm이다. 손님은 6cm만큼의 길이를 가져간다.
손님이 왔을 때 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 
설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.
'''

def binary_search_solution(n, target_cm:int, array:list[int]):

    start_cm = 0
    end_cm = max(array)
    mid_cm = 0

    while start_cm < end_cm:

        mid_cm = (start_cm + end_cm) // 2

        result_cm = 0
        for e in array:
            result_cm += e - mid_cm if e - mid_cm > 0 else 0

        if result_cm == target_cm:
            break
        
        elif result_cm > target_cm:
            start_cm = mid_cm + 1
        
        else:
            end_cm = mid_cm - 1

    print(mid_cm)

def first_try_solution(n, target_cm:int, array:list[int]):

    '''
    brute force 방식 
    '''

    array.sort(reverse=True)

    start_cm = array[0]
    while start_cm > 0:

        split_cm = 0
        for element in array:
            
            rest_cm = element - start_cm
            split_cm += rest_cm if rest_cm > 0 else 0

        if split_cm >= target_cm:
            break

        start_cm -= 1

    print(start_cm)

def main(input:str):
    
    lines = input.splitlines()
    n, target_cm = map(int, lines[0].split())

    array = list(map(int, lines[1].split()))

    #first_try_solution(n, target_cm, array)
    binary_search_solution(n, target_cm, array)

if __name__ == '__main__':

    question = '''
4 6
19 15 10 17
'''

    question = question.strip()

    main(question)