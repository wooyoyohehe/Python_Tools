#Linked List

# Generally speaking, how you use the linked_list depends on how you define it.
# For example, you can use both val and data to express its contents.

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Definition for singly-linked list.
# Demo from Leetcode
# Demo starts here
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# l1 and l2 are both nodes
# creates a new instance of the class and assigns this object to the local variable l1.
# 0 means the data in this node's cargo is 0
l1 = ListNode(0)
print l1.val

l2 = ListNode(1)
l1.next = l2
print l1.next.val
# Demo over


# Another demo created by myself
l3 = LinkedList()
n1 = Node(5)
print n1.data
n2 = Node(10)


# By Judging the node is None or not, we can get to know whether this linked_list is over or not.
print n1.next == None

# If we want to combine two linked_lists, we can do the follwering operation:
n1.next = n2
print n1.next == None



# In this instance, we define 4 nodes and link them together as a linked_list like this, and try to print all the elements in it:
# Define 4 nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

# Link them together:
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Tip: sometimes, we can assign one more node to keep the first node, in order to return.
node = node1
# print all them out:
def print_linklist(node):
    while node != None:
    # Or while node:
        print node.data
        node = node.next

print_linklist(node)

# What if we want to remove node4?
# Make the first node refer to the third
node3.next = node4.next
# separate the second node from the rest of the list
node4.next = None

new_node = Node(2.5)
# What if we want to insert a new node between node2 and node3?
# Step 1
new_node.next = node3
# Step 2
node2.next = new_node
print_linklist(node)









