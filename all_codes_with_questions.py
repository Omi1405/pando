######################################################################
# SLIP NO. 1
######################################################################

# Q1. Write a Python program to append a new item to the end of the array. [10M]
arr = [10, 20, 30, 40]
print("Array:", arr)
n = int(input("Enter item: "))
arr.append(n)
print("Updated array:", arr)

# Q2. Write a python program to simulate a ticket booking system using queue where people are served in the order they arrived. [15M]
queue = []
while True:
    print("1. Add person  2. Serve person  3. Display  4. Exit")
    ch = input("Choice: ")
    if ch == "1":
        queue.append(input("Person name: "))
    elif ch == "2":
        if queue:
            print("Serving:", queue.pop(0))
        else:
            print("Queue is empty")
    elif ch == "3":
        print("Queue:", queue)
    else:
        break


######################################################################
# SLIP NO. 2
######################################################################

# Q1. Write a Python program to reverse the order of the elements in the array. [10M]
arr = [10, 20, 30, 40, 50]
print("Original:", arr)
arr.reverse()
print("Reversed:", arr)

# Q2. Write a Python program to search a specific element in a singly linked list and return true if the item is found otherwise return false. [15M]
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

key = int(input("Enter item to search: "))
current = head
found = False
while current:
    if current.data == key:
        found = True
        break
    current = current.next
print(found)


######################################################################
# SLIP NO. 3
######################################################################

# Q1. Write a Python program to calculate sum of all odd numbers in an array. [10M]
arr = [1, 2, 3, 4, 5, 6, 7]
total = 0
for n in arr:
    if n % 2 != 0:
        total += n
print("Sum of odd numbers:", total)

# Q2. Write a Python program to delete the last item from a singly linked list. [15M]
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

if head is None:
    print("List is empty")
elif head.next is None:
    head = None
else:
    current = head
    while current.next.next:
        current = current.next
    current.next = None

current = head
while current:
    print(current.data, end=" ")
    current = current.next


######################################################################
# SLIP NO. 4
######################################################################

# Q1. Write a Python program to implement Static implementation of stack of integers. [10M]
MAX = 5
stack = []
while True:
    print("1.Push 2.Pop 3.Display 4.Exit")
    ch = input("Choice: ")
    if ch == "1":
        if len(stack) < MAX:
            stack.append(int(input("Enter number: ")))
        else:
            print("Stack Overflow")
    elif ch == "2":
        if stack:
            print("Popped:", stack.pop())
        else:
            print("Stack Underflow")
    elif ch == "3":
        print(stack)
    else:
        break

# Q2. Write a Python program to delete a specific item from a given doubly linked list. [15M]
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

head = Node(10)
b = Node(20); c = Node(30)
head.next = b; b.prev = head
b.next = c; c.prev = b

key = int(input("Item to delete: "))
cur = head
while cur and cur.data != key:
    cur = cur.next
if cur:
    if cur.prev:
        cur.prev.next = cur.next
    else:
        head = cur.next
    if cur.next:
        cur.next.prev = cur.prev
else:
    print("Item not found")

cur = head
while cur:
    print(cur.data, end=" ")
    cur = cur.next


######################################################################
# SLIP NO. 5
######################################################################

# Q1. Write a Python program to sort a list of elements using the insertion sort algorithm. [10M]
arr = [5, 2, 4, 1, 3]
for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key
print("Sorted:", arr)

# Q2. Write a Python program to accept an infix expression, convert it into its equivalent prefix expression and display the result. (Use Static implementation of Stack). [15M]
expr = input("Enter expression (single letters/numbers, no spaces): ")
rev = expr[::-1].swapcase()
stack = []
out = ""
prec = {'+':1, '-':1, '*':2, '/':2, '^':3}
for ch in rev:
    if ch.isalnum():
        out += ch
    elif ch == ')':
        stack.append(ch)
    elif ch == '(':
        while stack and stack[-1] != ')':
            out += stack.pop()
        if stack: stack.pop()
    else:
        while stack and stack[-1] != ')' and prec.get(stack[-1], 0) > prec.get(ch, 0):
            out += stack.pop()
        stack.append(ch)
while stack:
    out += stack.pop()
print("Prefix:", out[::-1])


######################################################################
# SLIP NO. 6
######################################################################

# Q1. Write a Python program to sort a list of elements using selection sort algorithm. [10M]
arr = [64, 25, 12, 22, 11]
for i in range(len(arr)):
    m = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[m]:
            m = j
    arr[i], arr[m] = arr[m], arr[i]
print("Sorted:", arr)

# Q2. Write a Python program to sort a stack using an auxiliary stack. [15M]
stack = [4, 1, 3, 2]
aux = []
while stack:
    x = stack.pop()
    while aux and aux[-1] > x:
        stack.append(aux.pop())
    aux.append(x)
print("Sorted stack (bottom to top):", aux)


######################################################################
# SLIP NO. 7
######################################################################

# Q1. Write a Python program for binary search of an ordered list. [10M]
arr = [10, 20, 30, 40, 50, 60]
key = int(input("Enter number: "))
low, high = 0, len(arr) - 1
found = False
while low <= high:
    mid = (low + high) // 2
    if arr[mid] == key:
        found = True
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
print("Found" if found else "Not Found")

# Q2. Write a Python program to implement dynamic implementation of stack of integers. [15M]
stack = []
while True:
    print("1.Push 2.Pop 3.Display 4.Exit")
    ch = input("Choice: ")
    if ch == "1":
        stack.append(int(input("Enter number: ")))
    elif ch == "2":
        print("Popped:", stack.pop() if stack else "Stack is empty")
    elif ch == "3":
        print(stack)
    else:
        break


######################################################################
# SLIP NO. 8
######################################################################

# Q1. Write a Python program to sort a list of elements using Quick sort algorithm. [10M]
def quick_sort(a):
    if len(a) <= 1:
        return a
    pivot = a[len(a)//2]
    left = [x for x in a if x < pivot]
    mid = [x for x in a if x == pivot]
    right = [x for x in a if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)

arr = [8, 3, 1, 7, 0, 10, 2]
print("Sorted:", quick_sort(arr))

# Q2. Write a Python program to check whether the contents of two stacks are identical. [15M]
s1 = [10, 20, 30]
s2 = [10, 20, 30]
if s1 == s2:
    print("Stacks are identical")
else:
    print("Stacks are not identical")


######################################################################
# SLIP NO. 9
######################################################################

# Q1. Write a Python program to sort a list of elements using the merge sort algorithm. [10M]
def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    result = []
    while left and right:
        result.append(left.pop(0) if left[0] < right[0] else right.pop(0))
    return result + left + right

arr = [38, 27, 43, 3, 9, 82, 10]
print("Sorted:", merge_sort(arr))

# Q2. Write a Python program to read a postfix expression, evaluate it and display the result. (Use Static implementation of Stack). [15M]
expr = input("Enter postfix (example 23+): ")
stack = []
for ch in expr:
    if ch.isdigit():
        stack.append(int(ch))
    else:
        b = stack.pop()
        a = stack.pop()
        if ch == '+': stack.append(a + b)
        elif ch == '-': stack.append(a - b)
        elif ch == '*': stack.append(a * b)
        elif ch == '/': stack.append(a // b)
print("Result:", stack[-1])


######################################################################
# SLIP NO. 10
######################################################################

# Q1. Write a Python program to calculate sum of all odd numbers in an array. [10M]
arr = [1, 2, 3, 4, 5, 6, 7]
total = 0
for n in arr:
    if n % 2 != 0:
        total += n
print("Sum of odd numbers:", total)

# Q2. Write a Python program to accept an infix expression, convert it into its equivalent postfix expression and display the result. (Use Static implementation of Stack). [15M]
expr = input("Enter infix (example A+B*C): ")
stack = []
out = ""
prec = {'+':1, '-':1, '*':2, '/':2, '^':3}
for ch in expr.replace(" ", ""):
    if ch.isalnum():
        out += ch
    elif ch == '(':
        stack.append(ch)
    elif ch == ')':
        while stack and stack[-1] != '(':
            out += stack.pop()
        if stack: stack.pop()
    else:
        while stack and stack[-1] != '(' and prec.get(stack[-1], 0) >= prec.get(ch, 0):
            out += stack.pop()
        stack.append(ch)
while stack:
    out += stack.pop()
print("Postfix:", out)


######################################################################
# SLIP NO. 11
######################################################################

# Q1. Write a Python program to sort a list of elements using Quick sort algorithm. [10M]
def quick_sort(a):
    if len(a) <= 1: return a
    pivot = a[len(a)//2]
    return quick_sort([x for x in a if x < pivot]) + [x for x in a if x == pivot] + quick_sort([x for x in a if x > pivot])
arr = [9, 4, 7, 3, 10, 5]
print(quick_sort(arr))

# Q2. Write a Python program that accepts the vertices and edges of a graph. Create adjacency list and display the adjacency list. [15M]
vertices = input("Enter vertices separated by space: ").split()
graph = {v: [] for v in vertices}
edges = int(input("Number of edges: "))
for _ in range(edges):
    a, b = input("Enter edge (u v): ").split()
    graph[a].append(b)
    graph[b].append(a)
print("Adjacency list:")
for v in graph:
    print(v, ":", graph[v])


######################################################################
# SLIP NO. 12
######################################################################

# Q1. Write a Python program to sort a list of elements using the insertion sort algorithm. [10M]
arr = [9, 5, 1, 4, 3]
for i in range(1, len(arr)):
    key = arr[i]; j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j+1] = arr[j]; j -= 1
    arr[j+1] = key
print("Sorted:", arr)

# Q2. Write a Python program to create a doubly linked list, append some items and iterate through the list (print forward). [15M]
class Node:
    def __init__(self, data):
        self.data = data; self.prev = None; self.next = None

head = tail = None
for x in [10, 20, 30]:
    node = Node(x)
    if head is None: head = tail = node
    else:
        tail.next = node; node.prev = tail; tail = node
cur = head
while cur:
    print(cur.data, end=" ")
    cur = cur.next


######################################################################
# SLIP NO. 13
######################################################################

# Q1. Write a program to find the length of a singly linked list. [10M]
class Node:
    def __init__(self, data):
        self.data = data; self.next = None
head = Node(10); head.next = Node(20); head.next.next = Node(30)
count = 0; cur = head
while cur:
    count += 1; cur = cur.next
print("Length:", count)

# Q2. Write a Python program which accepts the string and check whether the string is Palindrome or not using stack. (Use Static implementation of Stack). [15M]
text = input("Enter string: ")
stack = list(text)
rev = ""
while stack:
    rev += stack.pop()
if text == rev:
    print("Palindrome")
else:
    print("Not Palindrome")


######################################################################
# SLIP NO. 14
######################################################################

# Q1. Write a Python program to get the number of occurrences of a specified element in an array. [10M]
arr = [10, 20, 10, 30, 10, 40]
n = int(input("Enter number: "))
print("Occurrences:", arr.count(n))

# Q2. Write a Python program to create a doubly linked list and print nodes from current position to first node. [15M]
class Node:
    def __init__(self, data):
        self.data = data; self.prev = None; self.next = None
a = Node(10); b = Node(20); c = Node(30)
a.next = b; b.prev = a; b.next = c; c.prev = b
cur = c
while cur:
    print(cur.data, end=" ")
    cur = cur.prev


######################################################################
# SLIP NO. 15
######################################################################

# Q1. Write a python program to implement a circular queue. [10M]
class CircularQueue:
    def __init__(self, size):
        self.size = size; self.q = [None]*size
        self.front = self.rear = -1
    def enqueue(self, x):
        if (self.rear + 1) % self.size == self.front:
            print("Queue Full"); return
        if self.front == -1: self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.q[self.rear] = x
    def display(self):
        print(self.q)
q = CircularQueue(5)
q.enqueue(10); q.enqueue(20); q.enqueue(30)
q.display()

# Q2. Write a function in python to display an element from BST. [15M]
class Node:
    def __init__(self, data):
        self.data = data; self.left = self.right = None
root = Node(20); root.left = Node(10); root.right = Node(30)
key = int(input("Enter item: "))
def search(node, key):
    if node is None: return False
    if node.data == key: return True
    if key < node.data: return search(node.left, key)
    return search(node.right, key)
print("Found" if search(root, key) else "Not Found")


######################################################################
# SLIP NO. 16
######################################################################

# Q1. Write a Python program to create a Binary Search tree for string data. [10M]
class Node:
    def __init__(self, data):
        self.data = data; self.left = self.right = None
def insert(root, word):
    if root is None: return Node(word)
    if word < root.data: root.left = insert(root.left, word)
    elif word > root.data: root.right = insert(root.right, word)
    return root
root = None
for word in ["mango", "apple", "pear", "banana"]:
    root = insert(root, word)
def inorder(node):
    if node:
        inorder(node.left); print(node.data); inorder(node.right)
inorder(root)

# Q2. Write a python program to implement circular queue of integers using list. [15M]
size = 5
q = [None] * size
front = rear = -1
def enqueue(x):
    global front, rear
    if (rear + 1) % size == front:
        print("Queue Full")
    else:
        if front == -1: front = 0
        rear = (rear + 1) % size
        q[rear] = x
def display():
    if front == -1: print("Queue Empty")
    else:
        i = front
        while True:
            print(q[i], end=" ")
            if i == rear: break
            i = (i + 1) % size
        print()
enqueue(10); enqueue(20); enqueue(30); display()


######################################################################
# SLIP NO. 18
######################################################################

# Q1. Write a program to remove duplicate elements from an unsorted linked list. [10M]
class Node:
    def __init__(self, data):
        self.data = data; self.next = None
head = Node(10); head.next = Node(20); head.next.next = Node(10); head.next.next.next = Node(30)
seen = set(); cur = head; prev = None
while cur:
    if cur.data in seen:
        prev.next = cur.next
    else:
        seen.add(cur.data); prev = cur
    cur = cur.next
cur = head
while cur:
    print(cur.data, end=" "); cur = cur.next

# Q2. Write a Python program to implement a Binary search tree (BST) with operations – create, count the total nodes and total leaf nodes in the tree. [15M]
class Node:
    def __init__(self, data):
        self.data = data; self.left = self.right = None
root = Node(20); root.left = Node(10); root.right = Node(30); root.left.left = Node(5)
def count_nodes(n):
    return 0 if n is None else 1 + count_nodes(n.left) + count_nodes(n.right)
def count_leaves(n):
    if n is None: return 0
    if n.left is None and n.right is None: return 1
    return count_leaves(n.left) + count_leaves(n.right)
print("Total nodes:", count_nodes(root))
print("Leaf nodes:", count_leaves(root))


######################################################################
# SLIP NO. 19
######################################################################

# Q1. Write a Python program that accepts the vertices and edges of a graph and store it as an adjacency matrix. Implement functions to print indegree, outdegree and total degree of all vertices of graph. [10M]
n = int(input("Number of vertices: "))
matrix = [[0]*n for _ in range(n)]
edges = int(input("Number of directed edges: "))
for _ in range(edges):
    u, v = map(int, input("Enter edge u v (0-based): ").split())
    matrix[u][v] = 1
for i in range(n):
    outdegree = sum(matrix[i])
    indegree = sum(matrix[j][i] for j in range(n))
    print(i, "In:", indegree, "Out:", outdegree, "Total:", indegree + outdegree)

# Q2. Write a python program to Implement Dynamic implementation of Queue for integers. [15M]
queue = []
while True:
    print("1.Enqueue 2.Dequeue 3.Display 4.Exit")
    ch = input("Choice: ")
    if ch == "1":
        queue.append(int(input("Enter number: ")))
    elif ch == "2":
        print("Removed:", queue.pop(0) if queue else "Queue is empty")
    elif ch == "3":
        print(queue)
    else:
        break


######################################################################
# SLIP NO. 21
######################################################################

# Q1. Write a Python program to implement a Binary search tree (BST) with operations – create, insert and inorder. [10M]
class Node:
    def __init__(self, data):
        self.data = data; self.left = self.right = None
def insert(root, x):
    if root is None: return Node(x)
    if x < root.data: root.left = insert(root.left, x)
    elif x > root.data: root.right = insert(root.right, x)
    return root
def inorder(root):
    if root:
        inorder(root.left); print(root.data, end=" "); inorder(root.right)
root = None
for x in [50, 30, 70, 20, 40]:
    root = insert(root, x)
inorder(root)

# Q2. Write a Python program to search a specific item in a given doubly linked list and return true if the item is found otherwise return false. [15M]
class Node:
    def __init__(self, data):
        self.data = data; self.prev = None; self.next = None
a = Node(10); b = Node(20); c = Node(30)
a.next = b; b.prev = a; b.next = c; c.prev = b
key = int(input("Search item: "))
cur = a; found = False
while cur:
    if cur.data == key:
        found = True; break
    cur = cur.next
print(found)


######################################################################
# SLIP NO. 22
######################################################################

# Q1. Write a Python program to implement a Binary search tree (BST) with operations – create, Insert and preorder. [10M]
class Node:
    def __init__(self, data):
        self.data = data; self.left = self.right = None
def insert(root, x):
    if root is None: return Node(x)
    if x < root.data: root.left = insert(root.left, x)
    elif x > root.data: root.right = insert(root.right, x)
    return root
def preorder(root):
    if root:
        print(root.data, end=" "); preorder(root.left); preorder(root.right)
root = None
for x in [50, 30, 70, 20, 40]:
    root = insert(root, x)
preorder(root)

# Q2. Write a Python program for the implementation of Topological sorting. [15M]
from collections import defaultdict, deque
n = int(input("Number of vertices: "))
m = int(input("Number of edges: "))
graph = defaultdict(list); indegree = [0]*n
for _ in range(m):
    u, v = map(int, input("Enter directed edge u v: ").split())
    graph[u].append(v); indegree[v] += 1
q = deque(i for i in range(n) if indegree[i] == 0)
order = []
while q:
    u = q.popleft(); order.append(u)
    for v in graph[u]:
        indegree[v] -= 1
        if indegree[v] == 0: q.append(v)
print("Topological order:", order if len(order) == n else "Cycle exists")


######################################################################
# SLIP NO. 23
######################################################################

# Q1. Write a Python program to implement a Binary search tree (BST) with operations – create, insert and postorder. [10M]
class Node:
    def __init__(self, data):
        self.data = data; self.left = self.right = None
def insert(root, x):
    if root is None: return Node(x)
    if x < root.data: root.left = insert(root.left, x)
    elif x > root.data: root.right = insert(root.right, x)
    return root
def postorder(root):
    if root:
        postorder(root.left); postorder(root.right); print(root.data, end=" ")
root = None
for x in [50, 30, 70, 20, 40]:
    root = insert(root, x)
postorder(root)

# Q2. Write a Python program to insert an item in front of a given doubly linked list. [15M]
class Node:
    def __init__(self, data):
        self.data = data; self.prev = None; self.next = None
head = Node(20); second = Node(30)
head.next = second; second.prev = head
new_node = Node(10)
new_node.next = head
head.prev = new_node
head = new_node
cur = head
while cur:
    print(cur.data, end=" "); cur = cur.next


######################################################################
# SLIP NO. 24
######################################################################

# Q1. Write a Python program to implement a Binary search tree (BST) with operations – create, search, insert. [10M]
class Node:
    def __init__(self, data):
        self.data = data; self.left = self.right = None
def insert(root, x):
    if root is None: return Node(x)
    if x < root.data: root.left = insert(root.left, x)
    elif x > root.data: root.right = insert(root.right, x)
    return root
def search(root, x):
    if root is None or root.data == x: return root is not None
    if x < root.data: return search(root.left, x)
    return search(root.right, x)
root = None
for x in [50, 30, 70, 20, 40]: root = insert(root, x)
key = int(input("Search item: "))
print("Found" if search(root, key) else "Not Found")

# Q2. Write a Python program to reverse each word of the string by using static implementation of stack.
#   Example: Input - Welcome to class.   Output – .ssalc ot emocleW [15M]
text = input("Enter string: ")
stack = list(text)
result = ""
while stack:
    result += stack.pop()
print("Reversed:", result)


######################################################################
# SLIP NO. 25
######################################################################

# Q1. Write a python program for linear search. [10M]
arr = [10, 20, 30, 40, 50]
key = int(input("Enter number: "))
found = False
for x in arr:
    if x == key:
        found = True
        break
print("Found" if found else "Not Found")

# Q2. Write a python program to find the height and depth of a binary tree. [15M]
class Node:
    def __init__(self, data):
        self.data = data; self.left = self.right = None
root = Node(1)
root.left = Node(2); root.right = Node(3)
root.left.left = Node(4); root.left.right = Node(5)
def height(node):
    if node is None: return -1
    return 1 + max(height(node.left), height(node.right))
def depth(node, key, d=0):
    if node is None: return -1
    if node.data == key: return d
    left = depth(node.left, key, d+1)
    return left if left != -1 else depth(node.right, key, d+1)
key = int(input("Enter node value: "))
print("Height of tree:", height(root))
print("Depth of node:", depth(root, key))
