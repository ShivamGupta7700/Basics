while True:
    menu = int(input('''Which function would you like to perform?
1 - Find length of a dictionary
2 - Find value of the elements in the dictionary
3 - Find key of the elements in the dictionary
4 - Add an element to the dictionary
5 - Add multiple elements to the dictionary
6 - Update an element in a specific key
7 - Remove an element from the dictionary
8 - Find frequency of a value in the dictionary
9 - Reverse the dictionary (by key order)
10 - Sort the dictionary by key in ascending order
11 - Sort the dictionary by key in descending order
12 - Find the maximum, minimum key in the dictionary
13 - EXIT
Enter your choice : '''))

    if menu == 1:
        D = eval(input("Enter a dictionary: "))
        length = len(D)
        print("Length of the given dictionary is:", length)

    elif menu == 2:
        D = eval(input("Enter a dictionary: "))
        print("Keys of the given value are: ", D.values())

    elif menu == 3:
        D = eval(input("Enter a dictionary: "))
        print("Keys of the given value are: ", D.keys())

    elif menu == 4:
        D = eval(input("Enter a dictionary: "))
        key = input("Enter the key to be added: ")
        value = input("Enter the value to be added: ")
        D[key] = value
        print("New dictionary:", D)

    elif menu == 5:
        D = eval(input("Enter a dictionary: "))
        D1 = eval(input("Enter the dictionary to be added: "))
        D.update(D1)
        print("Updated dictionary:", D)

    elif menu == 6:
        D = eval(input("Enter a dictionary: "))
        key = input("Enter the key to be updated: ")
        value = input("Enter the new value: ")
        D[key] = value
        print("Updated dictionary:", D)

    elif menu == 7:
        D = eval(input("Enter a dictionary: "))
        key = input("Enter the key of the element to be removed: ")
        if key in D:
            del D[key]
            print("Updated dictionary:", D)
        else:
            print("Key not found")

    elif menu == 8:
        D = eval(input("Enter a dictionary: "))
        value = input("Enter the value to be counted: ")
        count = list(D.values()).count(value)
        print(f"Frequency of the given value: {count}")

    elif menu == 9:
        D = eval(input("Enter a dictionary: "))
        rev_dict = dict(reversed(list(D.items())))
        print("Reversed dictionary (by key order):", rev_dict)

    elif menu == 10:
        D = eval(input("Enter a dictionary: "))
        sorted_dict = dict(sorted(D.items()))
        print("Sorted dictionary by keys in ascending order:", sorted_dict)

    elif menu == 11:
        D = eval(input("Enter a dictionary: "))
        sorted_dict = dict(sorted(D.items(), reverse=True))
        print("Sorted dictionary by keys in descending order:", sorted_dict)

    elif menu == 12:
        D = eval(input("Enter a dictionary: "))
        if D:
            print("Maximum key:", max(D))
            print("Minimum key:", min(D))
        else:
            print("Dictionary is empty")

    elif menu == 13:
        print("Exiting the program...")
        break
