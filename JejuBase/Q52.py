# 퀵정렬
# 한값을 기준으로 자기보다 작은 수는 왼쪽에 큰 수는 오른쪽에 정렬시키는 알고리즘 

def 퀵정렬(입력리스트):
    입력리스트의길이 = len(입력리스트)
    if 입력리스트의길이 <= 1:
        return 입력리스트 
    기준값 = 입력리스트.pop(입력리스트의길이//2)
    그룹_하나 = []
    그룹_둘 = []

    for i in range(입력리스트의길이-1):
        if 입력리스트[i] < 기준값:
            그룹_하나.append(입력리스트[i])
            print(f"그룹하나 : {그룹_하나}")
        else:
            그룹_둘.append(입력리스트[i])
            print(f"그룹둘 : {그룹_둘}")
    return 퀵정렬(그룹_하나) + [기준값] + 퀵정렬(그룹_둘)


주어진리스트 = input().split(' ')
주어진리스트 = [int(i) for i in 주어진리스트]

print(퀵정렬(주어진리스트))