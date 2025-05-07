class Node:
    def __init__(self, value: int):
        self.value = value
        self.next: Node = None

class LinkedList:
    def __init__(self):
        self.first: Node = None
        self.last: Node = None

    def push(self, value):
        node = Node(value)

        if not self.last:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
    
    def print(self):
        aux = self.first

        while aux:
            print(aux.value)
            aux = aux.next

def merge_sort(linked_list: LinkedList):
    if linked_list.first is None or linked_list.first.next is None:
        return linked_list
    
    left, right = split_linked_list(linked_list)
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    return merge(sorted_left, sorted_right)
    
def split_linked_list(linked_list: LinkedList):
    slow = linked_list.first
    fast = linked_list.first
    prev = None

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    
    left = LinkedList()
    right = LinkedList()

    left.first = linked_list.first
    right.first = slow

    if prev:
        prev.next = None

    left.last = find_last_node(left.first)
    right.last = find_last_node(right.first)

    return left, right

def find_last_node(start_node):
    if not start_node:
        return None
        
    current = start_node

    while current.next:
        current = current.next

    return current

def merge(left: LinkedList, right: LinkedList):
    dummy = Node(0)
    tail = dummy

    l1 = left.first
    l2 = right.first

    while l1 and l2:
        if l1.value <= l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next

        tail = tail.next

    tail.next = l1 if l1 else l2

    merged = LinkedList()
    merged.first = dummy.next
    merged.last = find_last_node(merged.first)

    return merged

def test():
    linked_list = LinkedList()
    linked_list.push(3)
    linked_list.push(2)
    linked_list.push(1)
    linked_list.push(5)
    linked_list.push(4)

    print("Original:")
    linked_list.print()

    sorted_linked_list = merge_sort(linked_list)

    print("\nSorted:")
    sorted_linked_list.print()

test()