
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete_node_at_position(self, position):
        if position == 0:
            if self.head:
                self.head = self.head.next
            else:
                print("The list is empty.")
            return

        current = self.head
        prev = None
        count = 0

        while current and count != position:
            prev = current
            current = current.next
            count += 1

        if current:
            prev.next = current.next
        else:
            print("Invalid position.")

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def calculate_sum(self):
        current = self.head
        total = 0

        while current:
            total += current.data
            current = current.next

        return total

    def orta_aritmetik(self):
        num = self.head
        num1 = self.head

        while num1 and num1.next:
            num = num.next
            num1 = num1.next.next

        return num.data if num1 else None

    def insert_at_position(self, position, data):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        prev = None
        count = 0

        while current and count < position:
            prev = current
            current = current.next
            count += 1

        if count == position:
            prev.next = new_node
            new_node.next = current
        else:
            print("Invalid position.")



