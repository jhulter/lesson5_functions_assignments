# Task 1
# Task 2
#
# # Task 3
shopping_list = []
needs_more_items = True
needs_less_items = False
add_item = ""
remove_item = ""

def add_items():
    add_item = str(input("What would you like to add to your shopping list? "))
    shopping_list.append(add_item)

def subtract_item():
    remove_item = str(input("What would you like to remove from your list? "))
    shopping_list.remove(remove_item)
def action():
    pass

def print_list():
    print(f"Your shopping list contains {shopping_list}")

while needs_more_items == True:
    answer = str(input("Do you want to add or remove any items from your list(add/remove/done)? "))
    if answer == "done":
        needs_more_items = False
        needs_less_items = False
        print_list()
    elif answer == "add":
        needs_more_items = True
        needs_less_items = False
        add_items()
        print_list()
    elif answer == "remove":
        subtract_item()
        print_list()
    else:
        print("Invalid option")
        print_list()







