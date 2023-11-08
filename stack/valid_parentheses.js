/**
 * https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1361/
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {

    let stack = [];

    for (let c of s) {
        let top = stack[stack.length - 1];
        if (top && (top === '(' && c === ')') ||
            (top === '[' && c === ']') ||
            (top === '{' && c === '}')) {
            stack.pop();
        } else {
            stack.push(c);
        }
    }
    return stack.length === 0;

};

console.log(isValid("()[]{}"))
console.log(isValid("(]"))