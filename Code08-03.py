## 함수 선언부

class TreeNode() :
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None





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
            if current.left == None:
                current.left == node
                break
            current = current.left
        else :
            if current.right == None:
                current.right == node
                break 
            current = current.right
            
    memory.append(node)




print('이진 탐색 트리 구성 완료')