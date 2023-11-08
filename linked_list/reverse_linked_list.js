/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function (head) {
    let p = null;
    let c = head;

    while (c != null) {
        let temp = c.next;
        c.next = p;
        p = c;
        c = temp;
    }

    return p;
};