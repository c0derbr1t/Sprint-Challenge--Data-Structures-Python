import time
from bst import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

# My Work
duplicate_names = []
def sort_tree():
    middle = len(names_1) / 2
    rounded = round(middle)
    starting_point = names_1[rounded]
    global tree
    tree = BSTNode(starting_point)
    for name in names_1:
        tree.insert(name)

def check():
    for name in names_2:
        if tree.contains(name):
            duplicate_names.append(name)

def sort_and_check():
    start_timer = time.time()
    sort_tree()
    check()
    end_timer = time.time()
    print(f"{len(duplicate_names)} duplicate names:\n\n{', '.join(duplicate_names)}\n")
    print(f"My runtime: {end_timer - start_timer} seconds\n\n")

sort_and_check()

end_time = time.time()
print (f"{len(duplicates)} original duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"original runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
