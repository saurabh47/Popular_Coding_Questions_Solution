import MyLinkedList from './linked_list.js';

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var detectCycle = function (head) {
    let meet = detectCycleNode(head);
    let slow = head;

    if (meet == null) return null;

    while (slow != meet) {
        slow = slow.next;
        meet = meet.next;
    }

    return slow;
};

var detectCycleNode = function (head) {
    let slow = head;
    let fast = head;

    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next ? fast.next.next : null;
        if (slow == fast) {
            return slow;
        }
    }

    return null;
}


let cyclicLinkedList = new MyLinkedList();
cyclicLinkedList.addAtHead(3);
let p1 = cyclicLinkedList.addAtTail(2);
cyclicLinkedList.addAtTail(0);
let tail = cyclicLinkedList.addAtTail(4);
tail.next = p1;
console.log(detectCycle(cyclicLinkedList.head));