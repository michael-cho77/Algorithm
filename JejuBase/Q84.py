'''
test = [1, 2, 3, 4, 5, 6]

# 순열: 위치가 다르다면 다른 개체로 인식
print(list(permutations(test, 2)))

# 조합 : 위치가 달라도 내용물이 같다면 같은 개체로인식
print(list(combinations(test, 2)))
'''

from itertools import permutations


user_input = input()
k = int(input())
l =[i for i in user_input]
'''
for i in user_input:
    l.append(i)
'''
print(max(list(map(''.join, permutations(l, k)))))