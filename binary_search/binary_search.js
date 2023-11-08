/**
 * Binary search
 * @param {Number[]} nums  
 * @param {Number} target 
 * @returns index of the target number if found otherwise returns -1 
 */
function binarySearch(nums, target) {
    let left = 0, right = nums.length - 1;

    while (left <= right) {
        let mid = left + Math.floor((right - left) / 2);

        if (nums[mid] === target) {
            return mid;
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1;
}
/**
 * Nums [1,2,3,4,5,6,7]
 * Target 4
 */
console.log(binarySearch([1, 2, 3, 4, 5, 6, 7], 4));