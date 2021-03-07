# 리스트 [1,2,3,...,n] 를 섞는 방법은 총 n! 가지이다.
# n과 k가 주어졌을 때, k번째 섞은 결과를 반환하시오. (단, 1 <= n <= 9, 1 <= k <= n!)

import math

def solution(n, k):
    start = list(range(1, n+1))
    result = []
    for i in range(n,1,-1):
        if k >= math.factorial(i):
            index = k//math.factorial(i)
            result.append(start[index])
            del start[index]
            k -= math.factorial(i*index)

    result = result + start
    return result

n, k = map(int, (input().split()))

print(solution(n, k))