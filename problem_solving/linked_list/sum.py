from data_structures import Node


def sum_lists(ll_a: Node, ll_b: Node) -> Node:

    n1, n2 = ll_a, ll_b
    ll = head = None
    carry = 0
    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next

        node = Node(result % 10)

        if ll is None:
            ll = head = node
        else:
            ll = ll.next = node

        carry = result // 10

    if carry:
        ll = ll.next = Node(carry)

    return head
