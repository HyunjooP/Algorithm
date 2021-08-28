## 함수 선언부

from typing import Deque



def isQueueFull() :
    global SIZE, queue, front, rear
    if ( (rear+1)%SIZE == front) :
        return True
    else :
        return False

def isQueueEmpty() :
    global SIZE, queue, front, rear
    if (front == rear) :
        return True
    else :
        return False


def enQueue(data) :
    global SIZE, queue, front, rear
    if(isQueueFull()) :
        print('큐 꽉~')
        return
    rear = (rear +1) % SIZE
    queue[rear] = data


def deQueue():
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
         print('큐가 꽉 참')
         return None
    front = (front + 1) % SIZE
    data = queue[front] 
    queue[front] = None
    return data


## 전역 변수부

SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = 0        # 일반 큐와 원형 큐 차이점




## 메인 코드부

enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')

print('<--', queue, '<--')

data = deQueue(); print('디큐 :', data)
data = deQueue(); print('디큐 :', data)
data = deQueue(); print('디큐 :', data)
data = deQueue(); print('디큐 :', data)

print('<--', queue, '<--')