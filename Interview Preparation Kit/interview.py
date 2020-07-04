class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def checkBST(root):
    return (find(root, [-1]))


def find(root, prev):
    result = True

    if root.left:
        result = find(root.left, prev)

    if prev[0] >= root.data:
        return False

    prev[0] = root.data
    if root.right:
        result &= find(root.right, prev)

    return result


tree = BinarySearchTree()
t = 6

arr = [1, 2, 4, 3, 5, 6, 7]
for i in range(t):
    tree.create(arr[i])

ans = checkBST(tree.root)

print(ans)