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
    
print("Стек на основі масиву:")
stack_array = StackArray()
stack_array.push([85, 90, 78])
stack_array.push([88, 76, 92])
stack_array.push([91, 82, 79])
while not stack_array.is_empty():
    print(stack_array.pop())