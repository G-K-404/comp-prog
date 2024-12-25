from collections import deque
# Assuming root is a node in the tree and is structured as:
#root.val = data in root
#root.left = left child
#root.right = right child
def levelorder(root):
    q = deque()
    q.append(root)
    lot = []
    while(q):#as long as there are elements we iterate, each iteration is each level
        size = len(q)#number of nodes in current level
        level = []#contains all nodes of current level
        for i in range(size):
            node = q.popleft()
            level.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        lot.append(level)
    return lot