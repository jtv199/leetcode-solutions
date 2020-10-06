# Python3 program to find maximum sum leaf to root
# path in Binary Tree

# A tree node structure
class node:
    def __init__(self):
        self.data = 0
        self.left = None
        self.right = None


# A utility function that prints all nodes
# on the path from root to target_leaf
def printPath(root, target_leaf):
    # base case
    if (root == None):
        return False

    # return True if this node is the target_leaf
    # or target leaf is present in one of its
    # descendants
    if (root == target_leaf or
            printPath(root.left, target_leaf) or
            printPath(root.right, target_leaf)):
        print(root.data, end=" ")
        return True

    return False


max_sum_ref = 0
target_leaf_ref = None


# This function Sets the target_leaf_ref to refer
# the leaf node of the maximum path sum. Also,
# returns the max_sum using max_sum_ref
def getTargetLeaf(Node, curr_sum):
    global max_sum_ref
    global target_leaf_ref

    if (Node == None):
        return

    # Update current sum to hold sum of nodes on path
    # from root to this node
    curr_sum = curr_sum + Node.data

    # If this is a leaf node and path to this node has
    # maximum sum so far, then make this node target_leaf
    if (Node.left == None and Node.right == None):
        if (curr_sum > max_sum_ref):
            max_sum_ref = curr_sum
            target_leaf_ref = Node

            # If this is not a leaf node, then recur down
    # to find the target_leaf
    getTargetLeaf(Node.left, curr_sum)
    getTargetLeaf(Node.right, curr_sum)


# Returns the maximum sum and prints the nodes on max
# sum path
def maxSumPath(Node):
    global max_sum_ref
    global target_leaf_ref

    # base case
    if (Node == None):
        return 0

    target_leaf_ref = None
    max_sum_ref = -32676

    # find the target leaf and maximum sum
    getTargetLeaf(Node, 0)

    # print the path from root to the target leaf
    printPath(Node, target_leaf_ref);

    return max_sum_ref;  # return maximum sum


# Utility function to create a new Binary Tree node
def newNode(data):
    temp = node();
    temp.data = data;
    temp.left = None;
    temp.right = None;
    return temp;


# Function to insert nodes in level order
def insertLevelOrder(arr, root, i, n):
    # Base case for recursion
    if i < n:
        temp = newNode(arr[i])
        root = temp

        # insert left child
        root.left = insertLevelOrder(arr, root.left,
                                     2 * i + 1, n)

        # insert right child
        root.right = insertLevelOrder(arr, root.right,
                                      2 * i + 2, n)
    return root
# Driver function to test above functions

root = None;

# Constructing tree given in the above figure
testCases3 = [1,0,1,2,-1,3,2,1,4,0,3]
testCases = [770, 964, -720, 5, -360, -54, -987, -54, 948, 33, 47, -557, -461, -509, 846, 963, 423, 75, 236, -19, -284, -702, -396, -890, 189, 330, -991, 717, -453, -59, 267, 795, 838, -967, 417, -473, 363, 548, 796, -182, 8, 602, 370, 577, -343, -112, -405, -191, 148, -970, -312, -576, -706, 133, -456, -497, 750, 567, 88, -580, -434, 378, 376, -905, 169, 819, 68, -322, 48, -980, -92, -427, -135, -932, -143, 826, 547, -46, 408, 309, 706, -358, 937, -248, -290, 958, -883, -980, 214, 960, -737, 328, -188, -100, 697, -945, -402, 994, -812, -379, -757, 426, 185, 159, 685, -544, -551, 845, 767, 274, -152, 982, -119, -174, 855, -465, -571, -108, 657, -368]

root = insertLevelOrder(testCases,root,0,len(testCases))

print("Following are the nodes on the maximxum sum path ");
sum = maxSumPath(root);
print("\nSum of the nodes is ", sum);

# This code is contributed by Arnab Kundu