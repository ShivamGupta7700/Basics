while True:
    menu = int(input('''Which function would you like to perform?
1 - Find length of a tuple
2 - Create a tuple from a sequence data type
3 - Find index of an element in the tuple
4 - Add an element at the end of a tuple
5 - Add a tuple at the end of another tuple
6 - Insert an element in a specific position
7 - Remove an element from the tuple
8 - Find frequency of an element in the tuple
9 - Reverse the tuple
10 - Sort the tuple in ascending order
11 - Sort the tuple in descending order
12 - Find the minimum, maximum and sum of all elements in the tuple
13 - EXIT
Enter your choice : '''))

    if menu == 1:
        T = eval(input("Enter a tuple :"))
        length = len(T)
        print("Length of the given tuple is :", length)
    elif menu == 2:
        s = input("Enter a sequence :")
        T = tuple(s)
        print("Tuple :", T)
    elif menu == 3:
        T = eval(input("Enter a tuple :"))
        ch = input("Enter the element whose index number you want to know : ")
        index = T.index(ch)
        print("Index of the given element is : ", index)
    elif menu == 4:
        T = eval(input("Enter a tuple: "))
        L=list(T)
        element = input("Enter the element to be added: ")
        L.append(element)
        T1=tuple(L)
        print("New Tuple: ",T1)
    elif menu == 5:
        T = eval(input("Enter a tuple: "))
        T1 = tuple(input("Enter the tuple to be added : ").split(','))
        T = T + T1
        print("New tuple:", T)
    elif menu == 6:
        T = eval(input("Enter a tuple: "))
        L=list(T)
        ch=input("Enter the element to be inserted : ")
        pos=int(input("At which index? : "))
        L.insert(pos,ch)
        T1=tuple(L)
        print("New Tuple: ",T1)
    elif menu == 7:
        T = eval(input("Enter a tuple: "))
        ch = input("Enter the element to be removed : ")
        T = tuple(x for x in T if x != ch)
        print("New tuple : ", T)
    elif menu == 8:
        T = eval(input("Enter a tuple: "))
        ch = int(input("Enter the element to be counted : "))
        print("Frequency of the given element : ", T.count(ch))
    elif menu == 9:
        T = eval(input("Enter a tuple: "))
        T = T[::-1]
        print("Reversed tuple : ", T)
    elif menu == 10:
        T = eval(input("Enter a tuple: "))
        T = tuple(sorted(T))
        print("Sorted tuple in ascending order : ", T)
    elif menu == 11:
        T = eval(input("Enter a tuple: "))
        T = tuple(sorted(T, reverse=True))
        print("Sorted tuple in descending order : ", T)
    elif menu == 12:
        T = eval(input("Enter a tuple(integers): "))
        print("Maximum element : ", max(T))
        print("Minimum element : ", min(T))
        print("Sum of all the elements : ", sum(T))
    elif menu == 13:
        print("Exiting the program...")
        break
