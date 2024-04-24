class Stack {
    constructor() {
        this.items = []; // Initialize an empty array to store the stack elements
    }

    // Push: Add an element to the top of the stack
    push(element) {
        this.items.push(element);
    }

    // Pop: Remove and return the element from the top of the stack
    pop() {
        if (this.isEmpty()) {
            console.log("Stack is empty");
            return null;
        }
        return this.items.pop();
    }

    // Peek: Return the element at the top of the stack without removing it
    peek() {
        if (this.isEmpty()) {
            console.log("Stack is empty");
            return null;
        }
        return this.items[this.items.length - 1];
    }

    // isEmpty: Check if the stack is empty
    isEmpty() {
        return this.items.length === 0;
    }

    // Size: Return the number of elements in the stack
    size() {
        return this.items.length;
    }

    // Clear: Remove all elements from the stack
    clear() {
        this.items = [];
    }
}

// Example usage:
let stack = new Stack();

stack.push(1);
stack.push(2);
stack.push(3);

console.log("Stack size:", stack.size()); // Output: Stack size: 3
console.log("Top element:", stack.peek()); // Output: Top element: 3

console.log("Popped element:", stack.pop()); // Output: Popped element: 3
console.log("Popped element:", stack.pop()); // Output: Popped element: 2

console.log("Stack size:", stack.size()); // Output: Stack size: 1
