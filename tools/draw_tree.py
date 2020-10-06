class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)


def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root


def drawtree(root):
    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else -1

    def jumpto(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()

    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jumpto(x, y - 20)
            t.write(node.val, align='center', font=('Arial', 12, 'normal'))
            draw(node.left, x - dx, y - 60, dx / 2)
            jumpto(x, y - 20)
            draw(node.right, x + dx, y - 60, dx / 2)

    import turtle
    t = turtle.Turtle()
    t.speed(0);
    turtle.delay(0)
    h = height(root)
    jumpto(0, 60 * h)
    draw(root, 0, 60 * h, 80 * h)
    t.hideturtle()
    turtle.mainloop()

from random import randrange
testCases = [randrange(-5,5) for i in range(20)]
testCases2 = [770, 964, -720, 5, -360, -54, -987, -54, 948, 33, 47, -557, -461, -509, 846, 963, 423, 75, 236, -19, -284, -702, -396, -890, 189, 330, -991, 717, -453, -59, 267, 795, 838, -967, 417, -473, 363, 548, 796, -182, 8, 602, 370, 577, -343, -112, -405, -191, 148, -970, -312, -576, -706, 133, -456, -497, 750, 567, 88, -580, -434, 378, 376, -905, 169, 819, 68, -322, 48, -980, -92, -427, -135, -932, -143, 826, 547, -46, 408, 309, 706, -358, 937, -248, -290, 958, -883, -980, 214, 960, -737, 328, -188, -100, 697, -945, -402, 994, -812, -379, -757, 426, 185, 159, 685, -544, -551, 845, 767, 274, -152, 982, -119, -174, 855, -465, -571, -108, 657, -368]


if __name__ == '__main__':
    print(testCases)
    drawtree(deserialize(str(testCases2)))

