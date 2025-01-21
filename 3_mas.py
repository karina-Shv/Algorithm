class Node:
    def __init__(self, data=None, prev_index=None, next_index=None):
        self.data = data
        self.prev = prev_index
        self.next = next_index

class DoublyLinkedListArray:
    def __init__(self, size):
        self.size = size
        self.array = [None] * size
        self.head = None
        self.tail = None
        self.free_indices = list(range(size))

    def add(self, data):
        if not self.free_indices:
            print("List is full")
            return

        new_index = self.free_indices.pop(0)
        new_node = Node(data)
        self.array[new_index] = new_node

        if self.head is None:
            self.head = self.tail = new_index
        else:
            self.array[self.tail].next = new_index
            new_node.prev = self.tail
            self.tail = new_index

    def remove(self, data):
        current_index = self.head
        while current_index is not None:
            current_node = self.array[current_index]
            if current_node.data == data:
                if current_node.prev is not None:
                    self.array[current_node.prev].next = current_node.next
                else:
                    self.head = current_node.next

                if current_node.next is not None:
                    self.array[current_node.next].prev = current_node.prev
                else:
                    self.tail = current_node.prev

                self.array[current_index] = None
                self.free_indices.insert(0, current_index)
                return
            current_index = current_node.next
        print("Element not found")

    def display(self):
        current_index = self.head
        result = []
        while current_index is not None:
            current_node = self.array[current_index]
            result.append(current_node.data)
            current_index = current_node.next
        print("List:", result)

# Приклад використання
dll = DoublyLinkedListArray(5)
dll.add(10)
dll.add(20)
dll.add(30)
dll.display()

dll.remove(20)
dll.display()

dll.add(40)
dll.display()
