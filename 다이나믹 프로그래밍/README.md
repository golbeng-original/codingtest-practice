다이나믹 프로그래밍
==============
동적 계획법이라고도 표현하기도 한다.

다이나믹 프로그래밍은 큰 문제를 작은 문제로 쪼개서 문제를 해결하는 방법이다.

다이나믹 프로그래밍은 2가지 방식이 존재한다. `탑 다운`, `바텀 업`

```
가장 중요한 것은 주어진 문제가 다이나믹 푸로그래밍 유형인지를 파악하는 것이다.

1. 완전 탐색 알고리즘으로 접근 했을때 매우 오랜 시간 걸리는 경우
2. 나누어진 문제들이 중복되어 있는지 확인
```

<br/>
다이나믹 프로그래밍으로 해결할 수 있는 대표적인 예는 `피보나치 수열`이 있다.

> 점화식 <br/>
> 점화식이란 인접한 항들 사이의 관계식을 의히한다. <br/>

피보나치 수열의 점화식은 다음과 같이 표현할 수 있다.

$a_{n+2} = f(a_{n+1}, a_{n}) = a_{n+1} + a_n$

> 위와 같은 점화식은 3항간 점화식이라고 부른다. <br/>
> 인접한 총 3개의 항에 대해서 식이 정의되기 때문이다.

프로그래밍 내에서 처리
-----------------
프로그래밍에서는 이러한 수열을 `배열`, `리스트`로 표현할 수 있다.

수학적 점화식을 프로그래밍으로 표현하려면 재귀 함수를 사용하면 간단한다.

```python
def fibo(x):
    if x == 1 or x == 2:
        return 1
    
    return fibo(x - 1) + fibo(x - 2)

result = fibo(4)
```

하지만 피보나치 수열을 재귀 방식으로 처리하면 심각한 문제가 생길 수 있다.

n이 커진다면 수행시간이 기하급수적으로 늘어나고, stack overflow가 발생할 수 있다.

재귀 방식 다이나믹 프로그래밍 시간 복잡도는 $O(2^n)$ 이다.

다이나믹 프로그래밍 사용 조건
----------------------
1. 큰 문제를 작은 문제로 나눌 수 있다.
2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.

다이나믹 프로그램 특징
-----------------
분항 정복 알고리즘으로 분류되긴 하지만 분할 된 문제들이 다른 문제에 서로 영향을 미친다는 점이다.

다이나믹 프로그래밍은 한번 해결했던 문제를 다시금 해결한다는 점

메모제이션 기법
-----------
메모제이션은 다이나믹 프로그래밍을 구현하는 방법 중 한 종류로,

한번 구한 결과를 메모리 공간에 메모해두고 같은 식을 다시 호출하면 메모한 결괄르 그대로 가져오는 기법

메모제이션을 적용한 다이나믹 프로그래밍의 시간 복잡도는 $O(N)$ 이다.

```python

d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    
    if d[x] != 0:
        return d[x]
    
    d[x] = fibo(x - 1) + fibo(x - 2)

    return d[x]

result = fibo(99)
```

바텀-업 방식
=========
위에서 계속 설명하고 코드에 적혀 있는 방식은 탑-다운 방식이다.

큰 문제를 작은 문제를 호출하고 있는 형태이기 때문이다.

반면에 단순히 반복문을 이용하여 소스코드를 작성하는 경우 작은 문제부터 차근차근 답을

도출한다고 하여 `바텀-업 방식`이라고 한다.

```python
# 앞서 계산 된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 첫번째 피보나치 수와 두번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 99

for i in range(3, n + 1)
    d[i] = d[i - 1] + d[i - 2]

print(d[n])
```

> 바텀-업 방식에서 사용되는 결과 저장용 리스트는 `DP 테이블`이라고 부른다.

> 맵 형식 자료형을 사용할 수도 있다. <br/>
> 사전 자료형은 수열처럼 연속적이지 않은 경우에 유용하다.

다이나믹 프로그래밍 팁
-----------------
1. 일단 단순하게 재귀 함수로 비효율적인 프로그램을 작성(팁-다운)
2. 작은 문제에서 구한 답이 큰 문제에서 그대로 사용 할 수 있으면, 메모제이션 적용
3. 될 수 있으면, 바텀-업 방식으로 해결해보다.</br> 
(stack Overflow 발생을 방지하기 위해 재귀가 깊어져도 stack overFlow가 발생한다.)