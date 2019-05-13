def nth_from_last(head, n):
    """
    Get a linked list and return n-th value from the end

    :param head: Linked List
    :param n: Integer number
    :return:
    """
    left = right = head

    for i in range(n):
        if right is None:
            return None
        right = right.next

    while right:
        right = right.next
        left = left.next

    return left.value
