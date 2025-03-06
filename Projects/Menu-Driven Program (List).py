while True:
    menu=int(input('''Which function would you like to perform?
1 - Find length of a list
2 - Create a list from a sequence data type
3 - Find index of an element in the list
4 - Add an element at the end of a list
5 - Add a list at the end of another list
6 - Insert an element in a specific position
7 - Remove an element from the list
8 - Find frequency of an element in the list
9 - Reverse the list
10 - Sort the list in ascending order
11 - Sort the list in descending order
12 - Find the minimum, maximum and sum of all elements in the list
13 - EXIT
Enter your choice : '''))
    if menu==1:
        L=eval(input("Enter a list :"))
        length=len(L)
        print("Length of the given list is :", length)
    elif menu==2:
        s=input("Enter a sequence :")
        L=list(s)
        print("List :", L)
    elif menu==3:
        L=eval(input("Enter a list :"))
        ch=input("Enter the element whose index number you want to know : ")
        index=L.index(ch)
        print("Index of the given element is : ", index)
    elif menu==4:
       L = eval(input("Enter a list: "))
       element = input("Enter the element to be added: ")
       L.append(element) 
       print("New list:", L)
    elif menu==5:
        L = eval(input("Enter a list: "))
        L1 = input("Enter the list to be added : ").split(',')
        L.extend(L1) 
        print("New list:", L)
    elif menu==6:
        L = eval(input("Enter a list: "))
        ch=input("Enter the element to be inserted : ")
        pos=int(input("At which index? : "))
        L.insert(pos,ch)
        print("New list : ", L)
    elif menu==7:
        L = eval(input("Enter a list: "))
        ind=int(input("Enter the index of the element to be removed : "))
        L.pop(ind)
        print("New list : ", L)
    elif menu==8:
        L = eval(input("Enter a list: "))
        ch=int(input("Enter the element to be counted : "))
        print("Frequency of the gien element : ",L.count(ch))
    elif menu==9:
        L = eval(input("Enter a list: "))
        L.reverse()
        print("Reversed list : ", L)
    elif menu==10:
        L = eval(input("Enter a list: "))
        L.sort()
        print("Sorted list in ascending order : ",L)
    elif menu==11:
        L = eval(input("Enter a list: "))
        L.sort(reverse=True)
        print("Sorted list in descending order : ",L)
    elif menu==12:
        L = eval(input("Enter a list(integers): "))
        print("Maximum element : ",max(L))
        print("Minimum element : ",min(L))
        print("Sum of all the elements : ",sum(L))
    elif menu==13:
        print("Exiting the program...")
        break
