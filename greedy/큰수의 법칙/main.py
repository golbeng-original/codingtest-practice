'''
큰수의 법칙

다양한 수로 이루어진 배열이 있을때 주어진 수들을 M번 더하여 가장 큰수를 만드는 법칙이다.
단, 배열의 특정한 인덱스에 해당하는 수가 연속 K번을 초과하여 더해질수 없는 것이 이법칙의 특징

순서가 2,4,5,4,6 으로 이루어진 배열이 있을 떄 M이 8이고, K가 3이라고 가정하자.
결과는 6+6+6+5+6+6+6+5 = 46 이 된다.
'''

'''
5개의 데이터가 있고
8번을 더해야 하고,
3번을 연속할 수 있다.
'''



def main(input:str):

    lines = input.splitlines()
    n, m, k  = map(int, lines[0].split())
    datas = list(map(int, lines[1].split()))

    #print(f'n = {n}, m = {m}, k = {k}')
    #rint(datas)

    # 전톡적인 방식 버블 소트
    for i in range(0, len(datas) - 1 ):
        for j in range(i+1, len(datas)):

            if datas[i] < datas[j]:
                datas[i], datas[j] = datas[j], datas[i]

    total_number = 0
    curr_idx = 0
    for i in range(1, m+1):
        
        total_number = total_number + datas[curr_idx]

        # 첫번쨰 인덱스가 k만큼 반복했나?
        # 두번째 인덱스가 한번 사용되었나?
        if i % k == 0 or curr_idx == 1:
            curr_idx = (curr_idx + 1) % 2
        
    print(f'result = {total_number}')

if __name__ == '__main__':

    input:str = '5 8 3\n2 4 5 4 6'
    main(input)