/**
 * @param {character[]} letters
 * @param {character} target
 * @return {character}
 */
var nextGreatestLetter = function (letters, target) {
    let left = 0, right = letters.length - 1;
    while (left <= right) {
        let mid = left + Math.floor((right - left) / 2);

        if (letters[mid] <= target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return letters[left % letters.length];
};

console.log(nextGreatestLetter(["c", "f", "j"], "a"));
console.log(nextGreatestLetter(['a', 'b'], "z"));
console.log(nextGreatestLetter(["c", "f", "j"], "c"));