class BST:
    def __init__(self):
        self.root = None
    def insert(self):
        Data = input('이진트리에 추가할 데이터를 입력해 주세요 : ')
        if self.root == None:
            self.root = bstNode(Data)
        else:
            self.root.insertNode(Data)
    def height(self):
        if self.root == None:
            return -1
        else:
            return self.root.height()
    
class bstNode:
    def __init__(self,Data=None):
        self.data = Data
        self.parent = None
        self.left = None
        self.right = None
    def insertNode(self,Data):
        newNode = bstNode(Data)
        if self.data > Data:
            if self.left == None:
                self.left = newNode
                newNode.parent = self
            else:
                self.left.insertNode(Data)
        elif self.data < Data:
            if self.right == None:
                self.right = newNode
                newNode.parent = self
            else:
                self.right.insertNode(Data)
        else:
            print('{} 는 이미 해당 Tree안에 존재합니다.'.format(Data))
    def height(self):
        if self.left != None:
            _left = self.left.height()
        else:
            _left =  -1
        if self.right != None:
            _right = self.right.height()
        else:
            _right = -1
        return 1+max(_left,_right)

#일단 유효한 값을 입력 받아야만 재귀함수가 실행될 수 있다.(None(Null)이나 [] 같은 경우 height 라는 메소드가 없기 때문에 위의 코드처럼
#None값에 대해서 재귀함수를 호출해야할 경우 논리 혹은 예외처리로 체크해준다.
