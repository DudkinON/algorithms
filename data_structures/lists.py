from data_structures import Node


class LinkedList(object):

    def __init__(self, value=None):
        if not value:
            self.head = None
        else:
            self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = self.head
            self.length += 1
            return self

        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        return self

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return self

    def insert(self, index, value):

        if index > self.length or index == self.length:
            self.append(value)
            return self

        if index == 0:
            self.prepend(value)
            return self

        new_node = Node(value)
        parent = self.get_parent(index)
        child = parent.next
        parent.next = new_node
        new_node.next = child
        child.prev = new_node

        self.length += 1
        return self

    def remove(self, index):

        if index > self.length - 1:
            return self

        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return self

        parent = self.get_parent(index)

        child = parent.next

        if not child.next:
            self.tail = parent

        parent.next = child.next

        del child

        self.length -= 1

        return self

    def pop(self):
        if self.length == 1:
            val = self.tail.value
            self.head = None
            self.tail = None
            self.length = 0
            return val
        elif self.length == 0:
            return None
        else:
            return self.remove(self.length - 1)

    def get_parent(self, index):
        parent = self.head

        i = 0

        while i < index - 1:
            parent = parent.next
            i += 1
        return parent

    def get_list(self):
        lst = list()
        current = self.head

        while current:
            lst.append(current.value)
            current = current.next

        return lst

    def reverse(self):

        if not self.head.next:
            return self

        parent = self.head
        self.tail = self.head
        child = parent.next

        while child:
            temp = child.next
            child.next = parent
            parent = child
            child = temp
        self.head.next = None
        self.head = parent
