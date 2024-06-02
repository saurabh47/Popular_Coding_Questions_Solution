


/*
Tree traversal

In computer science, tree traversal (also known as tree search) is a form of graph traversal and refers
to the process of visiting (checking and/or updating) each node in a tree data structure, 
exactly once. Such traversals are classified by the order in which the nodes are visited. 
The following algorithms are described for a binary tree, but they may be generalized to other
trees as well.

There are two categories of traversals:
1. Depth First Traversals:
(a) Inorder (Left, Root, Right)
(b) Preorder (Root, Left, Right)
(c) Postorder (Left, Right, Root)

2. Breadth First Traversal (Or Level Order Traversal)
    In Breadth First Traversal, the root node is visited first, then the nodes on the next level, then the nodes on the next level, and so on.
*/

#include<iostream>
using namespace std;

struct Node{
    int data;
    struct Node *left, *right;
};

struct Node* newNode(int data){
    struct Node* node = (struct Node*)malloc(sizeof(struct Node));
    node->data = data;
    node->left = node->right = NULL;
    return node;
}

Node* head = NULL;

void insert(int data){
    if(head == NULL){
        head = newNode(data);
        return;
    }
    if(data <= head->data){
        head = head->left;
    }else{
        head = head->right;
    }
    insert(data);
}

void search(int x){
    if(head == NULL){

    }
}

int main( int argc, char *argv[] ){
/*
    Given an array of integers the program
    should print array in inorder, preorder and postorder traversal.
*/

        // 1, 4, 2, 3, 5, 6, 7
             /*
              head
                 \
                 1
              /      \
            NULL      4
                    /
                   2
                    \
                     3
                      \
                       5
                        \
                         6
                          \
                           7
                            \
                            NULL
                */
    for(int i=1; i < argc; i++){
        int data = atoi(argv[i]);
        insert(data);
    }

    while(head != NULL){
        cout << head->data << " ";
        head = head->right;
    }
    return 0;
}