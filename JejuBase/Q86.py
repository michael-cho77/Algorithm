#접시점수 = [1, 1, 3, 2, 5]
접시점수 = [5, 2, 3, 1, 2, 5]
먹을접시위치 = 1

def solution(접시점수, 먹을접시위치):
    # 배열은 0부터 시작하므로 -1 해줌
    먹을접시위치 -= 1
    정답 = 0
    정렬된접시점수 = sorted(접시점수)
    
    while True:
        print(f'접시점수 : {접시점수}')
        print(f'정렬된접시점수 : {정렬된접시점수}')
        맨앞접시 = 접시점수.pop(0)
        print(f'맨앞접시 : {맨앞접시}')
        print(f'---------------------')

        if 정렬된접시점수[0] == 맨앞접시:
            if 먹을접시위치 == 0:
                break
            # 아니라면
            먹을접시위치 -= 1
            정렬된접시점수.pop(0)
        else:
            # 맨 앞의 요소를 pop해서 append로 뒤로보냄
            접시점수.append(맨앞접시)
            # 3항 연산자
            먹을접시위치 = len(접시점수) - 1 if 먹을접시위치 == 0 else 먹을접시위치 - 1
        정답 += 1
    return 정답



print(solution(접시점수, 먹을접시위치))


'''
3항 연산자 

print('if') if True else print('else')

'''


