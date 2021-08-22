## 함수 선언부
class Node() :
    def __init__(self) :        # 생성자
        self.data = None
        self.link = None

def printNodes(start) :
    current = start
    print(current.data, end=' ')
    while (current.link != None):
        current = current.link
        print(current.data, end=' ')
    print()
def insertNode(findData, insertData) :
    global memory, head, current, pre
    if head.data == findData :  # 첫번째 노드에 삽입
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        memory.append(node)
        return
    current = head
    while current.link != None : # 마지막 노드에 삽입
        pre = current
        current = current.link
        if current.data == findData :
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            memory.append(node)
            return
    node = Node()       # 마지막 노드에 삽입
    node.data = insertData
    current.link = node
    memory.append(node)
    return
def deleteNode(deleteData) :        # 노드에서 삭제
    global memory, head, current, pre
    if head.data == deleteData :
        current = head
        head = head.link
        del(current)
        return
    current = head
    while current.link != None :
        pre = current
        current = current.link
        if current = deleteData :
            pre.link = current.link
            del(current)
            return
def findNode(findData) :        # 노드 찾기
    global memory, head, current, pre
    if head.data == findData :
        current = head
        head = head.link
        return(findNode)
    current = head
    while current.link != None :
        pre = current
        current = current.link
        if current = findData :
            pre.link = current.link
            return







## 전역 변수부
memory = []     # 노드 저장 공간
head, current, pre = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효']



## 메인 코드부


node = Node()       # 첫번째 노드
node.data = dataArray[0]
head = node
memory.append(node)


for data in dataArray[1:] :
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)
printNodes(head)


# insertNode('다현', '화사')
# printNodes(head)
# insertNode('다현', '화사')
# printNodes(head)


deleteNode('쯔위')
printNodes(head)


