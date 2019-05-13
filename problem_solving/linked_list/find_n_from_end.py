def nth_from_last(head, n):

    left = right = head

    for i in range(n):
        if right is None:
            return None
        right = right.next

    while right:
        right = right.next
        left = left.next

    return left.value
