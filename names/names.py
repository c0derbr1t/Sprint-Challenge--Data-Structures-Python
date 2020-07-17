import time
from bst.bst import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure
tree_duplicates = []

# Replace the nested for loops below with your improvements
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

def name_tree():
    middle = len(names_1) / 2
    rounded = round(middle)
    start_tree = names_1[rounded]
    global tree
    tree = BSTNode(start_tree)
    for name in names_1:
        tree.insert(name)

def check():
    for name in names_2:
        if tree.contains(name):
            tree_duplicates.append(name)

def run_check():
    tree_start = time.time()
    name_tree()
    check()
    tree_end = time.time()
    print(f"{len(tree_duplicates)} tree_duplicates:\n\n{', '.join(tree_duplicates)}\n")
    print(f"tree runtime: {tree_end - tree_start} seconds\n\n")

run_check()

end_time = time.time()
print(f"{len(duplicates)} duplicates (original):\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds\n\n")



# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
