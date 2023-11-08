/**
 * https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1360/
 */
var MinStack = function () {
    this.stack = [];
};

/** 
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function (val) {
    let top = this.stack[this.stack.length - 1];
    this.stack.push({ val, min: (top && (top.min < val)) ? top.min : val });
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function () {
    this.stack.pop();
};

/**
 * @return {number}
 */
MinStack.prototype.top = function () {
    return this.stack[this.stack.length - 1] ? this.stack[this.stack.length - 1].val : null;
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function () {
    return this.stack[this.stack.length - 1] ? this.stack[this.stack.length - 1].min : null;
};

/** 
 * Your MinStack object will be instantiated and called as such:
 */
var obj = new MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
console.log(obj.getMin())
obj.pop()
console.log(obj.top())
console.log(obj.getMin())