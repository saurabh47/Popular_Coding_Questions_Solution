/**
 * Insertion Sort
 * Time Complexity -> O(n^2) (Best case -> O(n))
 * Space Complexity -> O(1)
 * This technique is useful for the partially sorted array
 * In case of sorted array time complexity will be O(n)
 * https://leetcode.com/problems/sort-an-array/
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArray = function (nums) {
    insertionSort(nums);
    return nums;
};

function insertionSort(arr) {
    let n = arr.length;

    for (let i = 1; i < n; i++) {
        let temp = arr[i];
        let j = i - 1;
        for (; j >= 0; j--) {
            if (arr[j] > temp) {
                arr[j + 1] = arr[j];
            } else {
                break;
            }
        }
        arr[j + 1] = temp;
    }
}



console.log(sortArray([5, 2, 3, 4, 1, 4]));