class Stack {
    constructor() {
        this.count = 0;
        this.storage = {};
    }

    push(value) {
        this.storage[this.count] = value;
        this.count ++;
    }

    pop() {
        if (this.count === 0) {
            return undefined;
        }
        this.count --;
        let result = this.storage[this.count]
        delete this.storage[this.count];
        return result
    }

    size() {
        return this.count;
    }

    peek() {
        return this.storage[this.count - 1]
    }
} 

let stack = new Stack()
stack.push("a")
stack.push("b")
stack.push("b")
stack.push("c")
stack.push("a")
console.log('stack.pop() :>> ', stack.pop());
console.log('stack.pop() :>> ', stack.pop());
console.log('stack.pop() :>> ', stack.pop());
console.log('stack.size() :>> ', stack.size());
console.log('stack.peek() :>> ', stack.peek());
console.log('stack.pop() :>> ', stack.pop());
console.log('stack.peek() :>> ', stack.peek());

console.log('stack.pop() :>> ', stack.pop());
console.log('stack.pop() :>> ', stack.pop());
