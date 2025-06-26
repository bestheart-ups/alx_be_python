def display_menu():
    print("shopping list manager")
    print("1, add item")
    print("2, remove item")
    print("3, view list")
    print("4, exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("emter your choice: ")

        if choice == "1":
            item = input("enter the item to add: ").strip()
            if item:
                 shopping_list.append(item)
        print(f'"{item}" has been added to your shopping list')

        if choice == "2":
           if not shopping_list:
            print("your shopping list is empty. nothing to remove.")
            continue
        item = input("enter the item tp remove: ").strip()
        if item in shopping_list:
            shopping_list.remove(item)
        print(f'"{item}" has been removed from shopping list.')

        if choice == "3":
            if shopping_list:
                print("your shopping list:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
        else:
            print("your shopping list is currently empty,")

        if choice == "4":
            print("goodbye!")
            break
        else:
            print("invalid choice, please try again.")
    if __name__ == "__main__":
        main()


            


