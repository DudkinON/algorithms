from data_structures import Node as LinkedList


def remove_duplicates(head: LinkedList) -> LinkedList:

    node = head
    _map = set()
    _map.add(node.value)

    while node.next:
        if node.next.value in _map:
            node.next = node.next.next
        else:
            _map.add(node.next.value)
            node = node.next

    return head
