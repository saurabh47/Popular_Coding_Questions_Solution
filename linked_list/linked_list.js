export class Node {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}

export default function MyLinkedList() {
    this.head = null;
    this.size = 0;
};
/** 
 * @param {number} index
 * @return {number}
 */
MyLinkedList.prototype.get = function (index) {
    let current = this.head;
    let count = 1;
    while (count <= index) {
        if (current == null) {
            return -1;
        }
        current = current.next;
        count++;
    }
    return current ? current.val : -1;
};

/** 
 * @param {number} val
 * @return {void}
 */
MyLinkedList.prototype.addAtHead = function (val) {
    let node = new Node(val);
    node.next = this.head;
    this.head = node;
    this.size++;
    return this.head;
};

/** 
 * @param {number} val
 * @return {void}
 */
MyLinkedList.prototype.addAtTail = function (val) {
    let current = this.head;

    if (this.size == 0) {
        this.addAtHead(val);
        return;
    }

    while (current.next != null) {
        current = current.next;
    }
    let node = new Node(val);
    current.next = node;
    this.size++;
    return node;
};

/** 
 * @param {number} index 
 * @param {number} val
 * @return {void}
 */
MyLinkedList.prototype.addAtIndex = function (index, val) {
    let prev = this.head;
    let count = 1;

    if (index === 0 || (this.size === 0 && index === 0)) {
        this.addAtHead(val);
        return;
    }

    if (index > this.size) {
        return;
    }

    while (count < index) {
        prev = prev.next;
        count++;
    }

    let node = new Node(val);
    node.next = prev.next;
    prev.next = node;
    this.size++;
};

/** 
 * @param {number} index
 * @return {void}
 */
MyLinkedList.prototype.deleteAtIndex = function (index) {
    if (index >= this.size) return;

    if (index === 0 && this.size === 1) {
        this.size--;
        this.head = null;
        return;
    }

    if (index === 0) {
        this.head = this.head.next;
        this.size--;
        return;
    }

    let prev = this.head;
    let count = 1;

    while (count < index) {
        prev = prev.next;
        count++;
    }

    prev.next = prev.next.next;
    this.size--;
};
/**
 * Your MyLinkedList object will be instantiated and called as such:
 * var obj = new MyLinkedList()
 * var param_1 = obj.get(index)
 * obj.addAtHead(val)
 * obj.addAtTail(val)
 * obj.addAtIndex(index,val)
 * obj.deleteAtIndex(index)
 */

// let linked = new MyLinkedList();

/**
 * ["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
 * * [[],[1],[3],[1,2],[1],[1],[1]]
 */

// linked.addAtHead(1); // 1
// linked.addAtTail(3); // 1 -> 3
// linked.addAtIndex(1, 2);// 1 -> 2 -> 3
// console.log(linked.get(1));
// linked.deleteAtIndex(1); // 1 -> 3
// console.log(linked.get(1));
// console.log(linked);
