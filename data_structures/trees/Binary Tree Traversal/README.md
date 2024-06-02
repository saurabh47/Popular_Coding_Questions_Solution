Tree Traversal = A process of visiting each node in a tree data structure exactly once. Traversal can be done in depth-first or breadth-first order.

Depth-first order = starts at the root (top) node of a tree and visits all the nodes down the current branch (path), then backtracks till it finds the nearest unexplored path. <br>
Breadth-first order = starts at the tree root and visits all the neighbor nodes at current depth before moving on to the nodes at the next depth level.

Binary tree = A tree in which each node has only two child nodes. The <b>Left</b> child holds value lesser than the parent, and the <b>Right</b> child holds value greater than parent. Consequently, the left subtree contains values lesser than the root, while the right subtree holds values greater than the root.

<img src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/2009/06/tree12.gif">

Preorder traversal, Inorder traversal, and post order traversal are methods of <b>depth-first tree traversal</b>.
Preorder = First visits root, then covers left subtree, and lastly moves to the right subtree. 
<ul>
<li>In the above example tree, root is 1. Program first starts at this root. 1 is visited.</li>
<li>Preorder function visits the left child of 1, the value 2 is visited. </li>
<li>3 is now considered the root of this subtree. Preorder function is called recursively to visit left child of 2. </li>
<li>4 is visited. Since 4 has no child nodes, function backtracks and visits 5.</li>
<li>5 is considered root of this subtree, and preorder function recursively traverses. </li>
</ul>
In this way, the preorder function visits left nodes till there are no child elements, then backtracks and visits the right child node of the earlier visited node.
The preorder output for this example tree would be:1 2 4 5 3

Inorder = First traverses the left-subtree, then visits root and lastly moves to the right subtree. 
<ul>
<li>In the above example tree, root is 1. Program first recursively traverses left subtree. 4 is visited.</li>
<li>Inorder function visits the parent of 4, which is the root for the subtree formed by 4. The value 2 is visited. </li>
<li>Right child of 2 is visited. 5 is visited. </li>
<li>Root of subtree created by 2,4,5 is visited. 1 is visited.</li>
<li>Inorder function then traverses right subtree in the same manner. </li>
</ul>
The inorder output for this example tree would be:4 2 5 1 3

Postorder = First traverses the left-subtree, then traverses the right subtree, and lastly visits root. 
<ul>
<li>In the above example tree, root is 1. Program first recursively traverses left subtree. 4 is visited.</li>
<li>Inorder function visits the right-subtree of parent of 4, value 5 is visited. </li>
<li>Root of subtree formed by 5 is visited. 2 is visited. </li>
<li>Postorder function then traverses right subtree in the same manner. Root 1 is visited at the end, after all nodes in right subtree are visited.</li>
</ul>
The postorder output for this example tree would be:4 5 2 3 1

<b>Code screenshots</b>
Input prompt: 
<img src="https://github.com/MansiAyer/Popular_Coding_Questions_Solution/blob/master/Binary%20Tree%20Traversal/prompt.JPG">

Input:
<img src="https://github.com/MansiAyer/Popular_Coding_Questions_Solution/blob/master/Binary%20Tree%20Traversal/input.JPG">

Input given: 6 4 8 2 1 5

Preorder output:
<img src="https://github.com/MansiAyer/Popular_Coding_Questions_Solution/blob/master/Binary%20Tree%20Traversal/preorder.JPG">

Inorder output:
<img src="https://github.com/MansiAyer/Popular_Coding_Questions_Solution/blob/master/Binary%20Tree%20Traversal/inorder.JPG">

Postorder output:
<img src="https://github.com/MansiAyer/Popular_Coding_Questions_Solution/blob/master/Binary%20Tree%20Traversal/postorder.JPG">
