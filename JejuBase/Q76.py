import numpy as np

사각형 = 5
탐색가능지역 = 3

지뢰밭 = [
    [1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0]]


지뢰밭 = np.array(지뢰밭)
#print(지뢰밭[0:3, 0:3])  #0~3줄까지, 0~3칸까지
#print(지뢰밭[0:3, 1:4])
#print(지뢰밭[0:3, 2:5])

#print(지뢰밭[1:4, 0:3])  
#print(지뢰밭[1:4, 1:4])
#print(지뢰밭[1:4, 2:5])


s = 0
for i in range(사각형 - 탐색가능지역 + 1):
    for j in range(탐색가능지역):
        print(i, 탐색가능지역+i )
        print(j, 탐색가능지역+j) 
        print('================')
        if np.sum(지뢰밭[i:탐색가능지역+i, j:탐색가능지역+j]) > s:
            s = np.sum(지뢰밭[i:탐색가능지역+i, j:탐색가능지역+j])

print(s)
