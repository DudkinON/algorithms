from data_structures import Node


def is_palindrome(ll: Node) -> bool:
    """
    Checks if linked list is a palindrome

    :param ll: Linked list (First node)
    :return: Boolean
    """
    cache = []
    node = ll

    while node:
        cache.append(node.value)
        node = node.next

    node = ll

    while node:
        num = cache.pop()
        if node.value != num:
            return False
        node = node.next

    return True
