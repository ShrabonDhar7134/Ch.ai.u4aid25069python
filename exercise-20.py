# Exercise 20: Shopping list manager

shopping_list = []

while True:
    choice = input("Choose action (add / remove / show / quit): ").lower()

    if choice == "add":
        item = input("Enter item name: ")
        shopping_list.append(item)
        print(item, "added to shopping list")

    elif choice == "remove":
        item = input("Enter item name to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(item, "removed from shopping list")
        else:
            print("Item not found")

    elif choice == "show":
        print("Shopping List:", shopping_list)

    elif choice == "quit":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid option, try again")
