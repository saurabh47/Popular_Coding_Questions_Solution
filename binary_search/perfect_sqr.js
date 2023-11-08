/**
 * Valid Perfect Square
 * https://leetcode.com/explore/learn/card/binary-search/137/conclusion/978/
 * @param {number} num
 * @return {boolean} returns true if the number is perfect square
 */
var isPerfectSquare = function (num) {
    let left = 0, right = num;

    while (left <= right) {
        let mid = left + Math.floor((right - left) / 2);
        let numSqr = mid * mid;
        if (numSqr === num) {
            return true;
        } else if (numSqr < num) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }

    }
    return false;
};

console.log(isPerfectSquare(16)) // TRUE
console.log(isPerfectSquare(10)) // FALSE