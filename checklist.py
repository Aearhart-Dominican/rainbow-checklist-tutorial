checklist = []

def create(item):
    checklist.append(item)

def read(index):
    item = checklist[index]
    return item

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)

def select(function_code: str):

    match function_code.capitalize():
        case "C":
            create(input("Enter Item: "))

        case "R":
            try:
                print(read(input("Enter Index: ")))
            except(ValueError, IndexError, TypeError):
                print("Invalid Index Input")

        case "P":
            print(checklist)
        
        case "U":
            try:
                index_input = int(input("Enter Item Index: "))
                item_input = input("Enter Updated Item: ")
                update(index_input, item_input)
            except(ValueError, IndexError):
                print("Invalid Index Input")
        
        case "D":
            try:
                print(destroy(int(input("Enter Index: "))))
            except(ValueError, IndexError, TypeError):
                print("Invalid Index Input")

        case "Q":
            return False
        
        case _:
            print("Unknown Option\n")
    return True

def list_all_items():
    index = 0
    for list_item in checklist:
        print(f"{index} {list_item} \n")
        index += 1

def mark_completed(index):
    update(index, "√" + checklist[index])

# this function is completely redundant, so I will just use input
def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    # print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
    # print(read(1))

    list_all_items()
    mark_completed(0)
    list_all_items()


running = True
while running:
    selection = input("Press C to add to list, R to read from list, P to display list, U to update list item, D to destroy item, and Q to quit: ")
    running = select(selection)