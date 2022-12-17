class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)  # bardzo ogólnie

    def __next__(self):
        return str(self.next)  # bardzo ogólnie


class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0  # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def is_empty(self):
        # return self.length == 0
        return self.head is None

    def count(self):  # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.head:  # dajemy na koniec listy
            node.next = self.head
            self.head = node
        else:  # pusta lista
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):  # klasy O(1)
        if self.head:  # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        else:  # pusta lista
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):  # klasy O(1)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:  # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None  # czyszczenie łącza
        self.length -= 1
        return node  # zwracamy usuwany node

    def remove_tail(self):  # klasy O(n)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.tail
        if self.tail == self.head:  # self.length == 1
            self.tail = self.head = None
        else:
            before = self.head
            curr = self.head.next
            while curr.next is not None:
                before = before.next
                curr = curr.next
            before.next = None
            self.tail = before

        node.next = None  # czyszczenie łącza
        self.length -= 1
        return node  # zwracamy usuwany node

    def join(self, other):
        if self.head:
            self.tail.next = other.head
            self.tail = other.tail
        else:
            self.head = other.head
            self.tail = other.tail
        self.length += other.length
        other.head = None
        other.tail = None
        other.length = 0  # klasy O(1)

    def clear(self):  # czyszczenie listy
        self.head = None
        self.tail = None
        self.length = 0


import unittest


class NodeTest(unittest.TestCase):
    def setUp(self):
        self.node = Node(3)

    def test_init(self):
        self.assertEqual(self.node.data, 3)
        self.assertEqual(self.node.next, None)

    def test_str(self):
        self.assertEqual(str(self.node), '3')


class SingleListTest(unittest.TestCase):
    def setUp(self):
        self.single_list = SingleList()
        self.node = Node(3)

    def test_is_empty(self):
        self.assertTrue(self.single_list.is_empty())

    def test_count(self):
        self.assertEqual(self.single_list.count(), 0)

    def test_insert_head(self):
        self.single_list.insert_head(self.node)
        self.assertEqual(self.single_list.count(), 1)
        self.assertEqual(self.single_list.head.data, 3)
        self.assertEqual(self.single_list.tail.data, 3)

    def test_insert_tail(self):
        self.single_list.insert_tail(self.node)
        self.assertEqual(self.single_list.count(), 1)
        self.assertEqual(self.single_list.head.data, 3)
        self.assertEqual(self.single_list.tail.data, 3)

    def test_remove_head(self):
        self.single_list.insert_head(self.node)
        self.assertEqual(self.single_list.remove_head().data, 3)
        self.assertEqual(self.single_list.count(), 0)

    def test_remove_tail(self):
        self.single_list.insert_tail(self.node)
        self.assertEqual(self.single_list.remove_tail().data, 3)
        self.assertEqual(self.single_list.count(), 0)

    def test_join(self):
        self.single_list.insert_tail(self.node)
        self.single_list_2 = SingleList()
        self.node_2 = Node(5)
        self.single_list_2.insert_tail(self.node_2)
        self.single_list.join(self.single_list_2)
        self.assertEqual(self.single_list.count(), 2)
        self.assertEqual(self.single_list.head.data, 3)
        self.assertEqual(self.single_list.tail.data, 5)

    def test_clear(self):
        self.single_list.insert_tail(self.node)
        self.single_list.clear()
        self.assertEqual(self.single_list.count(), 0)


if __name__ == '__main__':
    unittest.main()
