## 함수
def openbox() :
    global count
    print('상자열기')
    count -= -1
    if count == 0 :
        print('** 선물 넣기 **')
        return
    openbox()
    print('상자 닫기')
    



## 전역

count = 5



## 메인

openbox()