class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        # TODO: implement insert

    def find(self, value):
        # TODO: implement find

    def delete(self, value):
        # TODO: implement delete

    def inorder_traversal(self):
        result = []
        # TODO: implement inorder DFS
        return result


# ---------- TEST ----------
if __name__ == "__main__":
    bst = BinarySearchTree()
    for val in [10, 5, 15, 3, 7, 12, 18]:
        bst.insert(val)

    print("Inorder:", bst.inorder_traversal())  # Expected: [3, 5, 7, 10, 12, 15, 18]
    print("Find 7:", bst.find(7))  # Expected: True
    print("Find 20:", bst.find(20))  # Expected: False

    bst.delete(10)  # delete root with two children
    print("Inorder after deleting 10:", bst.inorder_traversal())  # Expected: sorted list without 10
