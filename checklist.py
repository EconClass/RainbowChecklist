# -*- coding: utf-8 -*-
# Initial Conditions
checklist = list()

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
        print(str(index) + str(list_item))
        index += 1

# Put a check on completed items in the list
def mark_completed(index):
    mark_item = checklist[index]
    print(str('√') + "{}".format(mark_item))

# Select functions to run
def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item: ")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = input("Index Number? ")
        # Remember that item_index must actually exist or our program will crash.
        print(read(item_index))

    # Print all items
    elif function_code == "P":
        list_all_items()

    # Stop the loop
    elif function_code == "Q":
        return False

    # Catch all
    else:
        print("Unknown Option")

    return True

# Prompt a user input
def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = raw_input(prompt)
    return user_input

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
    select("C")
    list_all_items()
    select("R")
    select("P")
    # select("Q")
    clear_terminal()

# Clear Terminal
def clear_terminal():
    import os
    os.system("clear")

# Run the test function
#test()

# Start Loop
running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list, P to display list, and Q to quit: ")
    running = select(selection)
