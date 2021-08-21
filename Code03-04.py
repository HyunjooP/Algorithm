## 함수 선언부

def add_data(friend):
    katok.append(None)
    kLen = len(katok)
    katok[kLen-1] = friend


def insert_data(position, friend) :
    
    katok.append(None)
    kLen = len(katok)

    for i in range(kLen-1, position, -1) :
        katok[i] = katok[i-1]
        katok[i-1] = None

    katok[position] = friend

def delete_data(position) :
    kLen = len(katok)
    katok[position] = None

    for i in range(position+1, kLen, 1) :
        katok[i-1] = katok[i]
        katok[i] = None

    del(katok[kLen-1])


## 전역 변수부
katok = []
select = -1     # 1.추가 2.삽입 3.삭제 4.종료







## 메인 코드부
while (select != 4):
    select = int(input("1.추가 2.삽입 3.삭제 4.종료-->"))

    if (select == 1) :
        pass
    elif (select == 2) :
        pass
    elif (select == 3) :
        pass
    elif (select == 4) :
        print(katok
        break
    else :
        print('다시 확인!')
        continue




