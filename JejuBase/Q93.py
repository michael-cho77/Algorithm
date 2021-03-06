# FIFO 가장 오랫동안 머무른 페이지를 교체 

def sol(frame, page):
    page = page.split(' ')
    runTime = 0
    temp = []

    if frame == 0:
        runTime = len(page) * 6
        return runTime
    
    for i in page:
        if i in temp:
            runTime += 1
        else:
            if len(temp) < frame:
                temp.append(i)
            else:
                temp = temp[1:] + [i]
            runTime += 6

    return runTime


print(sol(3, 'B C B A E B C E'))

#print(sol(3, ['B', 'C', 'B', 'A', 'E', 'B', 'C', 'E']))