
## 함수


def addNumber(num) :
    if num <= 1:
        return 1
    return num + addNumber(num-1)





## 전역



## 메인

print(addNumber(5))