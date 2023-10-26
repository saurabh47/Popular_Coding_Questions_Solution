/**
 * Quick Sort
 * Time Complexity -> Avg case -> O(nlog(n))
 * Space Complexity -> O(1)
 * https://leetcode.com/problems/sort-an-array/
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArray = function (nums) {
    quickSort(nums, 0, nums.length - 1);
    return nums
};

function quickSort(arr, s, e) {
    if (s >= e) return;

    let p = partition(arr, s, e);

    quickSort(arr, s, p);
    quickSort(arr, p + 1, e);
}

function partition(arr, s, e) {
    let pivot = arr[s];
    // Place pivot at correct position
    let cnt = 0;

    for (let i = s; i <= e; i++) {
        if (arr[i] < pivot) {
            cnt++;
        }
    }
    let pivotIdx = s + cnt;
    swap(arr, s, pivotIdx);

    let i = s, j = e;
    while (i < pivotIdx && pivotIdx < j) {
        while (arr[i] < pivot) {
            i++;
        }

        while (arr[j] >= pivot) {
            j--;
        }

        if (i < pivotIdx && j > pivotIdx) {
            swap(arr, i, j);
            i++;
            j--;
        }
    }

    return pivotIdx;
}

function swap(arr, s, d) {
    let t = arr[d];
    arr[d] = arr[s];
    arr[s] = t;
}

console.log(sortArray([5, 2, 3, 4, 1, 4]));