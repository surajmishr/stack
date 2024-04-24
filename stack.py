
# Explanation of the methods:

# is_empty(): Checks if the stack is empty.
# push(item): Adds an item to the top of the stack.
# pop(): Removes and returns the item at the top of the stack.
# peek(): Returns the item at the top of the stack without removing it.
# size(): Returns the number of elements in the stack.
# In the example usage, we create a stack object, push three elements onto the stack, peek at the top element, pop two elements, and check the size of the stack.


# Last-In, First-Out (LIFO

   Top
---------
|   3   |
---------
|   2   |
---------
|   1   |
---------
  Bottom
 top in first out 






class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty")
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty")
            return None

    def size(self):
        return len(self.items)

# Example usage:
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print("Stack size:", stack.size())  # Output: Stack size: 3
print("Top element:", stack.peek())  # Output: Top element: 3

print("Popped element:", stack.pop())  # Output: Popped element: 3
print("Popped element:", stack.pop())  # Output: Popped element: 2

print("Stack size:", stack.size())  # Output: Stack size: 1
