#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node *left;
    struct node *right;
};

struct node *tree;
void create_tree(struct node *);
struct node *insertElement(struct node *, int);
void preorderTraversal(struct node *);
void inorderTraversal(struct node *);
void postorderTraversal(struct node *);
int searchElement(struct node *, int);
void main()
{
    int option, val;
    struct node *ptr;
    create_tree(tree);
    do
    {
        printf("\n1.Insert element\n2.Preorder traversal\n3.Inorder traversal\n4.Postorder traversal\n5.Search a element\n6.EXIT");
        printf("\nEnter an option: ");
        scanf("%d", &option);
        switch (option)
        {
        case 1:
            printf("\nEnter the value of the new node: ");
            scanf("%d", &val);
            tree = insertElement(tree, val);
            break;

        case 2:
            printf("\nThe elements of the tree: ");
            preorderTraversal(tree);
            break;

        case 3:
            printf("\nThe elements of the tree: ");
            inorderTraversal(tree);
            break;

        case 4:
            printf("\nThe elements of the tree: ");
            postorderTraversal(tree);
            break;

        case 5:
            printf("\nEnter the value to be searched: ");
            scanf("%d", &val);
            searchElement(tree, val);
            break;
        }
    } while (option != 6);
}

void create_tree(struct node *tree)
{
    tree = NULL;
}

struct node *insertElement(struct node *tree, int val)
{
    struct node *ptr, *nodeptr, *parentptr;
    ptr = (struct node *)malloc(sizeof(struct node));
    ptr->data = val;
    ptr->left = NULL;
    ptr->right = NULL;
    if (tree == NULL)
    {
        tree = ptr;
        tree->left = NULL;
        tree->right = NULL;
    }
    else
    {
        parentptr = NULL;
        nodeptr = tree;
        while (nodeptr != NULL)
        {
            parentptr = nodeptr;
            if (val < nodeptr->data)
                nodeptr = nodeptr->left;
            else
                nodeptr = nodeptr->right;
        }
        if (val < parentptr->data)
            parentptr->left = ptr;
        else
            parentptr->right = ptr;
    }
    return tree;
}

void preorderTraversal(struct node *tree)
{
    if (tree != NULL)
    {
        printf("%d\t", tree->data);
        preorderTraversal(tree->left);
        preorderTraversal(tree->right);
    }
}

void inorderTraversal(struct node *tree)
{
    if (tree != NULL)
    {
        inorderTraversal(tree->left);
        printf("%d\t", tree->data);
        inorderTraversal(tree->right);
    }
}

void postorderTraversal(struct node *tree)
{
    if (tree != NULL)
    {
        postorderTraversal(tree->left);
        postorderTraversal(tree->right);
        printf("%d\t", tree->data);
    }
}

int searchElement(struct node *tree, int val)
{
    if (tree == NULL)
        printf("\nElement not  found");
    else if (tree->data == val)
        printf("\nElement found");
    else if (val < tree->data)
        return searchElement(tree->left, val);
    else if (val > tree->data)
        return searchElement(tree->right, val);
}
