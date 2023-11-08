/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
import MyLinkedList from './linked_list.js';

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function (head) {
    if (head == null) return false;

    let p1 = head;
    let p2 = head.next;

    while (p1 != null && p2 != null) {
        if (p1 === p2) {
            return true;
        }

        p1 = p1.next;
        p2 = p2.next ? p2.next.next : null;
    }
    return false;
};

var detectCycle = function (head) {
    if (head == null) return "no cycle";
    let items = new Set();

    let p = head;
    while (p != null) {
        if (items.has(p)) {
            // found the cycle
            let c = 0;
            let p2 = head;
            while (p2 != p) {
                p2 = p2.next
                c++;
            }
            return "tail connects to node index " + c;
        }
        items.add(p);
        p = p.next;
    }

    return "no cycle";
};

/**
 * without cycle
 */
let linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(2);
linkedList.addAtTail(3);
console.log(hasCycle(linkedList.head));

/**
 * with cycle
 */

let cyclicLinkedList = new MyLinkedList();
let head = cyclicLinkedList.addAtHead(1);
let tail = cyclicLinkedList.addAtTail(2);
tail.next = head;
console.log(hasCycle(cyclicLinkedList.head));
console.log(detectCycle(cyclicLinkedList.head));
