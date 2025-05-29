#Michael
#1/22/25
#To Do List
#init
groceryList = []
#Fun
def program():
    #Welcome

    print("Welcome to the Grocery List.")
    while True:
        try:
            print("What would you like to do?")
            print("1. View current list \n2. Add to list \n3. Remove from list \n4. Count the number of items on list \n5. Sort the list alphabetically \n6. Exit Program\n\n")
            action = int(input("Enter a number 1-6"))
            #Outcome of selected option
            #View
            if action == 1:
                print("Here is your list:")
                print(groceryList)
            #Add
            elif action == 2:
                print("What would you like to add to your list?")
                print(groceryList)
                item = input("Type your item here:")
                groceryList.append(item)
                print(item + " has been added to your list.")
                print(groceryList)
            #Remove
            elif action == 3:
                print("What item would you like remove?")
                print(groceryList)
                item = input("Type your item here:")
                groceryList.remove(item)
                print(item + " has been removed from your list.")
                print(groceryList)
            #Exit
            elif action == 6:
                print("Thank you for using the Grocery List.")
                break
            #Sort list
            elif action == 5:
                print("Sorting list")
                groceryList.sort()
                print("List sorted")
                print(groceryList)
        #Count and print items
            elif action == 4:
                print("Counting Items on list")
                num = len(groceryList)
                print("There are " + str(num) + " items on your list")
        except:
            print("please follow directions")

#Main
program()
