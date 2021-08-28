## 함수 선언부

class TreeNode() :
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None




## 전역 변수부
memory = []
root = None
nameAry = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']




## 메인 코드부
node = TreeNode()
node.data = nameAry[0]
root = node
memory.append(node)

for name in nameAry[1:] :   # 루트는 제외
    node = TreeNode()
    node.data = name

    current = root
    while True :
        if name < current.data :    
            if current.left == None:        # 왼쪽 노드가 비어있는지 확인하고
                current.left == node
                break
            current = current.left          # 안 비어있으면 왼쪽으로 내려감
        else :
            if current.right == None:       # 오른쪽 노드가 비어있는지 확인하고
                current.right == node
                break 
            current = current.right         # 안 비어있으면 오른쪽으로 내려감
            
    memory.append(node)


findData = '마마무'
current = root
while True :
    if current.data == findData :
        print(findData, ' 찾았음!')
        break
    elif findData < current.data :  # 값이 더 크면 왼쪽으로 가보자
        if current.left == None :       # 왼쪽이 비었으면
            print(findData, ' 없다 ㅠ')
            break
        current = current.left
    else :
        if current.right == None :      # 오른쪽이 비었으면
            print(findData, ' 없다 ㅠ')
            break
        current = current.right
    


print('이진 탐색 트리 구성 완료')