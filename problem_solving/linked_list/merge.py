from data_structures import Node


def merge_lists(list1: Node, list2: Node) -> Node:
    """
    Gets two sorted linked lists, and merges them. Returns
    sorted linked list

    :param list1: Linked list
    :param list2: Linked list
    :return: Linked list
    """

    if not list1:
        return list2

    if not list2:
        return list1

    if list1.value <= list2.value:
        node = list1
        node.next = merge_lists(list1.next, list2)
    else:
        node = list2
        node.next = merge_lists(list1, list2.next)

    return node
