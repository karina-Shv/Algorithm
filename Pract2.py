# Реалізація стеку на основі масиву
class StackArray:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None
    
    def size(self):
        return len(self.stack)

# Реалізація стеку на основі покажчиків
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None
    
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if not self.is_empty():
            data = self.top.data
            self.top = self.top.next
            return data
        return None
    
    def is_empty(self):
        return self.top is None
    
    def peek(self):
        if not self.is_empty():
            return self.top.data
        return None

# Реалізація двозв’язного списку на основі масиву
class DoublyLinkedListArray:
    def __init__(self):
        self.data = []
    
    def append(self, year, results):
        self.data.append((year, results))
    
    def analyze_trends(self):
        for i in range(len(self.data) - 2):
            avg1 = sum(self.data[i][1]) / len(self.data[i][1])
            avg2 = sum(self.data[i+1][1]) / len(self.data[i+1][1])
            avg3 = sum(self.data[i+2][1]) / len(self.data[i+2][1])
            print(f"{self.data[i][0]}-{self.data[i+2][0]}: {avg1:.2f} -> {avg2:.2f} -> {avg3:.2f}")

# Реалізація двозв’язного списку на основі покажчиків
class DoublyNode:
    def __init__(self, year, data):
        self.year = year
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedListPointer:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, year, data):
        new_node = DoublyNode(year, data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    def analyze_trends(self):
        current = self.head
        while current and current.next and current.next.next:
            avg1 = sum(current.data) / len(current.data)
            avg2 = sum(current.next.data) / len(current.next.data)
            avg3 = sum(current.next.next.data) / len(current.next.next.data)
            print(f"{current.year}-{current.next.next.year}: {avg1:.2f} -> {avg2:.2f} -> {avg3:.2f}")
            current = current.next

# Демонстрація роботи
if __name__ == "__main__":
    print("Стек на основі масиву:")
    stack_array = StackArray()
    stack_array.push([85, 90, 78])
    stack_array.push([88, 76, 92])
    stack_array.push([91, 82, 79])
    while not stack_array.is_empty():
        print(stack_array.pop())
    
    print("\nСтек на основі покажчиків:")
    stack_list = StackLinkedList()
    stack_list.push([85, 90, 78])
    stack_list.push([88, 76, 92])
    stack_list.push([91, 82, 79])
    while not stack_list.is_empty():
        print(stack_list.pop())
    
    print("\nДинаміка успішності (масив):")
    performance_array = DoublyLinkedListArray()
    performance_array.append(2020, [85, 90, 78])
    performance_array.append(2021, [88, 76, 92])
    performance_array.append(2022, [91, 82, 79])
    performance_array.append(2023, [93, 85, 88])
    performance_array.append(2024, [89, 87, 90])
    performance_array.analyze_trends()
    
    print("\nДинаміка успішності (покажчики):")
    performance_pointer = DoublyLinkedListPointer()
    performance_pointer.append(2020, [85, 90, 78])
    performance_pointer.append(2021, [88, 76, 92])
    performance_pointer.append(2022, [91, 82, 79])
    performance_pointer.append(2023, [93, 85, 88])
    performance_pointer.append(2024, [89, 87, 90])
    performance_pointer.analyze_trends()