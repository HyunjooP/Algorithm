# enQueue
size = 5
queue = [None for _ in range(size)]
front = rear = -1

rear += 1
queue[rear] = '화사'

rear += 1
queue[rear] = '솔라'

rear += 1
queue[rear] = '문별'


print(queue)



# deQueue

front += 1
data = queue[front]
queue[front] = None
print(data)

front += 1
data = queue[front]
queue[front] = None
print(data)

front += 1
data = queue[front]
queue[front] = None
print(data)

print(queue)


