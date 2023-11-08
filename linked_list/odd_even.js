/**
 * https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1208/
 */
import MyLinkedList from './linked_list.js';
import Node from './linked_list.js';
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
var oddEvenList = function (head) {
    if (head == null) return head;

    let p = head;
    let c = head.next;

    let e = new Node(-1, null);
    let n = e;

    while (c != null) {
        n.next = c;

        p.next = c.next;
        n = n.next;
        if (p.next == null) {
            break;
        }
        p = p.next;
        c = p.next;
    }
    if (n) {
        n.next = null;
    }

    p.next = e.next;

    return head;

};
let linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(2);
linkedList.addAtTail(3);
linkedList.addAtTail(4);
let r = oddEvenList(linkedList.head);
console.log(r);