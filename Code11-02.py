
import random 

## 함수 선언부
def findMinIndex(ary) :
    Minindex = 0
    for i in range(1, len(ary)) :
        if ( ary[Minindex] > ary[i] ) :
            Minindex = i
    return Minindex            



## 전역 변수부

before = [random.randint(33,190) for _ in range(20)]
after = []

# before의 개수만큼 반복
# 가장 작은 위치를 알아내기
# 가장 작은 값을 after에 넣고 before에서 지우기



## 메인 코드부

print('정렬 전 -->', before)
for _ in range(len(before)) :
    minPos = findMinIndex(before)
    after.append(before[minPos])
    del(before[minPos])
print('정렬 후 -->', after)