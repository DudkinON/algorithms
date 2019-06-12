from data_structures import Node as LinkedList


def remove_duplicates(head: LinkedList) -> LinkedList:
    """
    Removes duplicates from linked list

    :param head:
    :return:
    """

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


def remove_node(node: LinkedList) -> None:
    """
    Removes given node from linked list

    :param node:
    :return:
    """

    if node and node.next:
        node.value = node.next.value
        node.next = node.next.next


def intersection(a: LinkedList, b: LinkedList) -> LinkedList or None:

    cache, ll = set(), a

    while ll:
        cache.add(ll)
        ll = ll.next

    ll = b

    while ll:
        if ll in cache:
            return ll
        ll = ll.next

    return None
