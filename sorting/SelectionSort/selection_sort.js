/**
 * Selection Sort
 * Time Complexity -> O(n^2)
 * Space Complexity -> O(1)
 * https://leetcode.com/problems/sort-an-array/
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArray = function (nums) {
    selectionSort(nums);
    return nums
};

function selectionSort(arr) {
    let n = arr.length;
    for (let i = 0; i < n - 1; i++) {
        let minIdx = i;
        for (let j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
            }
        }
        swap(arr, i, minIdx);
    }
}

function swap(arr, s, d) {
    let t = arr[d];
    arr[d] = arr[s];
    arr[s] = t;
}

console.log(sortArray([5, 2, 3, 4, 1, 4]));