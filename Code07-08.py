## 함수 선언부

from typing import Deque



def isQueueFull() :
    global SIZE, queue, front, rear
    if (rear != SIZE-1) :
        return False
    elif (rear == SIZE-1) and (front == -1) :
        return True
    else :
        for i in range(front+1,SIZE) :
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
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
    rear += 1
    queue[rear] = data


def deQueue():
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
         print('큐가 꽉 참')
         return None
    front += 1
    data = queue[front] 
    queue[front] = None
    return data


## 전역 변수부

SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1




## 메인 코드부

enQueue('화사')
enQueue('솔라')
enQueue('문별')
print('<--', queue, '<--')

data = deQueue(); print('디큐 :', data)
data = deQueue(); print('디큐 :', data)
data = deQueue(); print('디큐 :', data)
data = deQueue(); print('디큐 :', data)
print('<--', queue, '<--')