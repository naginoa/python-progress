class Node():
    def __init__(self):
        self.data = '#'
        self.lchild = None
        self.rchild = None


class Tree(Node):
    def create(self, tree):
        data = input("->")
        if data == '#':
            tree = None
        else:
            tree.data = data
            tree.lchild = Node()
            self.create(tree.lchild)
            tree.rchild = Node()
            self.create(tree.rchild)

    def visit(self, tree):
        if tree.data != '#':
            print(tree.data)

    def pre_order(self, tree):
        if tree is not None:
            self.visit(tree)
            self.pre_order(tree.lchild)
            self.pre_order(tree.rchild)

    def in_order(self, tree):
        if tree is not None:
            self.in_order(tree.lchild)
            self.visit(tree)
            self.in_order(tree.rchild)

    def back_order(self, tree):
        if tree is not None:
            self.back_order(tree.lchild)
            self.back_order(tree.rchild)
            self.visit(tree)


t = Node()
tree = Tree()
tree.create(t)
tree.pre_order(t)
print('\n')
tree.in_order(t)
print('\n')
tree.back_order(t)