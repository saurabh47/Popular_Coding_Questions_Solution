/**
 * Merge Sort
 * Time Complexity -> Avg case -> O(nlog(n))
 * Space Complexity -> O(n)
 * https://leetcode.com/problems/sort-an-array/
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArray = function (nums) {
    mergeSort(nums, 0, nums.length - 1);
    return nums
};

function merge(arr, low, mid, high) {
    let temp = new Array(high - low + 1).fill();
    let p1 = low, p2 = mid + 1, idx = 0;

    while (p1 <= mid && p2 <= high) {
        if (arr[p1] < arr[p2]) {
            temp[idx++] = arr[p1++];
        } else {
            temp[idx++] = arr[p2++];
        }
    }

    while (p1 <= mid) temp[idx++] = arr[p1++];
    while (p2 <= high) temp[idx++] = arr[p2++];

    let k = low;
    for (let i = 0; i < high - low + 1; i++) {
        arr[k++] = temp[i];
    }
}

function mergeSort(arr, low, high) {
    if (low >= high) return;

    let mid = Math.floor((low + high) / 2);

    mergeSort(arr, low, mid);
    mergeSort(arr, mid + 1, high);

    merge(arr, low, mid, high);
}

console.log(sortArray([5, 2, 3, 4, 1, 4]));