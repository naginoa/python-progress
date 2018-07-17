class node():
    
    def __init__(self, root=None, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right

tree = node('d', node('b', node('a'), node('c')), node('e',right=node('g', left=node('f'))))
print(tree.left)

def pre_order(tree):
    if tree == None:
        return
        
    print(tree.root)
    pre_order(tree.left)
    pre_order(tree.right)
    
def mid_order(tree):
    if tree == None:
        return
    
    mid_order(tree.left)    
    print(tree.root)
    mid_order(tree.right)
    
def back_order(tree):
    if tree == None:
        return
        
    back_order(tree.left)
    back_order(tree.right)
    print(tree.root)
    
def floor_order(tree):
    if tree == None:
        return
    
    status = [tree]
    l = []
    while status :
        node = status.pop(0)
        if node.left:
            status.append(node.left)
        if node.right:
            status.append(node.right)
        l.append(node.root)
    print(l)

pre_order(tree)
mid_order(tree)
back_order(tree)
floor_order(tree)