import pytest
from bst import BinarySearchTree

# Contract:
# - No duplicates: inserting an existing value raises ValueError
# - find/delete on empty or missing value should not raise
# - inorder_traversal returns sorted list

def build_bst(vals):
    bst = BinarySearchTree()
    for v in vals:
        bst.insert(v)
    return bst

def test_empty_tree_ops():
    bst = BinarySearchTree()
    assert bst.find(1) is False
    bst.delete(1)  # should not raise
    assert bst.inorder_traversal() == []

def test_insert_find_inorder():
    bst = build_bst([10, 5, 15, 3, 7, 12, 18])
    assert bst.find(7) is True
    assert bst.find(99) is False
    assert bst.inorder_traversal() == [3, 5, 7, 10, 12, 15, 18]

def test_duplicate_insertion_policy():
    bst = build_bst([10, 5, 15])
    with pytest.raises(ValueError):
        bst.insert(10)
    with pytest.raises(ValueError):
        bst.insert(5)

def test_delete_leaf_one_child_two_children_and_root():
    # Start with full tree
    bst = build_bst([10, 5, 15, 3, 7, 12, 18])
    # delete leaf
    bst.delete(3)
    assert bst.inorder_traversal() == [5, 7, 10, 12, 15, 18]
    # delete node with one child
    bst.delete(12)
    assert bst.inorder_traversal() == [5, 7, 10, 15, 18]
    # delete root with two children
    bst.delete(10)
    inorder = bst.inorder_traversal()
    assert inorder == sorted(inorder) and 10 not in inorder

def test_skewed_tree_performance_smoke():
    # Insert sorted to create a skew; should still work functionally
    bst = build_bst([1,2,3,4,5,6,7,8,9])
    assert bst.inorder_traversal() == [1,2,3,4,5,6,7,8,9]
    # delete head/tail in skew
    bst.delete(1); bst.delete(9)
    assert bst.inorder_traversal() == [2,3,4,5,6,7,8]
