# 선택 정렬
import random



## -100보다 100까지 숫자를 랜덤하게 30개 만들기
## 내림 차순 정렬


def selectionSort(ary) :
    n = len(ary)
    for i in range(0, n-1):
        maxIndex = i
        for k in range(i+1, n) :
            if ary[maxIndex] < ary[k] :    
                maxIndex = k                    # k가 i보다 크면 최대값이 됨
        ary[i], ary[maxIndex] = ary[maxIndex], ary[i]   # i와 최대값의 위치를 바꿔주기

    return ary


dataAry = [random.randint(-100,101) for _ in range(30)]


print('정렬 전 -->', dataAry)
dataAry = selectionSort(dataAry)
print('정렬 후 -->', dataAry)