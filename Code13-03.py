## 함수

def binarysearch(ary, fdata) :
    pos = -1                        # 못 찾은 경우
    start = 0
    end = len(ary) - 1
    while (start <= end) :
        mid = (start+end) // 2      # 중앙에서 검색 시작
        if fdata == ary[mid] :      # 찾으려는 데이터와 일치하는 경우
            return mid
        elif fdata > ary[mid] :     # 중앙보다 값이 큰 경우
            start = mid+1           # 중앙+1로 검색 시작
        else : 
            end = mid - 1           #중앙보다 값이 작은 경우




    return pos



## 전역

dataAry = [50, 60, 105, 120, 150, 160, 162, 168, 177, 188]
findData = 162  # 할머니키

## 메인
print('배열-->', dataAry)
position = binarysearch(dataAry, findData)
if position == -1 :
    print('못 찾음')
else:
    print(findData, '는', position, '위치에 있음')