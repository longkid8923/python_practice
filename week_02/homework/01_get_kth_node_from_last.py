class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        end = self.head
        count = 0
        while end.next is not None:
            end = end.next
            count += 1
        print(count)
        print(count-k+1)

        cur = self.head
        for i in range(count - k + 1):
            cur = cur.next

        return cur


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)
linked_list.append(9)
linked_list.append(5)

print(linked_list.get_kth_node_from_last(5).data)  # 7이 나와야 합니다!