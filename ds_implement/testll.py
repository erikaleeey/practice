import pytest
from linkedlist import LinkedList

def test_empty_list_ops():
    ll = LinkedList()
    assert ll.find(1) is False
    ll.remove(1)  # should not raise
    ll.print_list()  # smoke test


def test_insert_on_empty_and_bounds():
    ll = LinkedList()
    ll.insert(0, 10)
    assert ll.find(10) is True
    with pytest.raises(IndexError):
        ll.insert(2, 99)
    with pytest.raises(IndexError):
        ll.insert(-1, 99)


def test_append_and_prepend_and_order():
    ll = LinkedList()
    ll.append(10); ll.append(20); ll.prepend(5)
    # expected: 5 -> 10 -> 20
    out = []
    cur = ll.head
    while cur:
        out.append(cur.value); cur = cur.next
    assert out == [5, 10, 20]

def test_insert_middle_and_tail():
    ll = LinkedList()
    for v in [5, 10, 20]:
        ll.append(v)
    ll.insert(1, 7)   # 5,7,10,20
    ll.insert(4, 25)  # append at end
    out = []
    cur = ll.head
    while cur:
        out.append(cur.value); cur = cur.next
    assert out == [5, 7, 10, 20, 25]

def test_remove_head_tail_and_duplicates():
    ll = LinkedList()
    for v in [5, 5, 10, 20, 20]:
        ll.append(v)
    ll.remove(5)      # remove first 5 only
    ll.remove(20)     # remove first 20 only
    out = []
    cur = ll.head
    while cur:
        out.append(cur.value)
        cur = cur.next
    assert out == [5, 10, 20]
    ll.remove(5)      # remove head
    ll.remove(20)     # remove tail
    out = []
    cur = ll.head
    while cur:
        out.append(cur.value); cur = cur.next
    assert out == [10]
