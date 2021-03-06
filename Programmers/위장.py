import collections

def solution(clothes):
    answer = 1
    kind = []

    for x, y in clothes:
        kind.append(y)
    
    kind = collections.Counter(kind)

    for i in kind.values():
        answer *= (i + 1)

    return answer -1
    

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]


print(solution(clothes))