## 함수 선언부



def isStackFull() :
    global SIZE, stack, top
    if (top >= SIZE-1) :
        return True
    else :
        return False

def push(data) :
    global SIZE, stack, top
    if (isStackFull()) :
        print("스택이 꽉 참")
        return
    top += 1
    stack[top] = data
    
def isStackEmpty() :
    global SIZE, stack, top
    if (top <= -1) :
        return True
    else :
        return False

def pop():
    global SIZE, stack, top    
    if (isStackEmpty()) :
        print("스택이 비어있음")
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data



## 전역 변수부
SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1







## 메인 코드부


# stack = ['커피', '녹차', '꿀물', '콜라', '환타']
# top = 4


push("커피1")
push("커피2")
print(stack)

data = pop()
print(data)
data = pop()
print(data)
data = pop()
print(data)

print(stack)