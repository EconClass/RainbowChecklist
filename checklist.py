# Initial Conditions
checklist = list()
# checklist.append("Hello")
# checklist.append("World")

# Create Items
def create(item):
    checklist.append(item)

# Read Items
def read(index):
    item = checklist[index]
    return item;

# Update Items
def update(index, item):
    checklist[index] = item

# Destroy Items
def destroy(index):
    checklist.pop(index)

# List Items
def list_all_items():
    index = 0
    for list_item in checklist:
        print(str(index) + list_item)
        index += 1

# Put a check on completed items in the list
def mark_completed(index):
    print(str(√) "{}".format(str(index)))

# Test Functions
def test():
    create("purple sox")
    create("red cloak")
    print(read(0))
    print(read(1))
    update(0, "purple socks")
    destroy(1)
    print(read(0))
    list_all_items()
    mark_completed(0)

test()
