#Python Final Project: Shopping List App
#Arjun Anand
#Created on 12/13

#The list
shoppingList = {"John": {
                "guitar" : 0,
                "speaker" : 0,
                "laptop" : 0,
                "budget" : 700,
                "status" : "incomplete"},

                "Christian": {
                "mouse" : 0,
                "clothes": 0,
                "games" : 0,
                "budget" : 80,
                "status" : "incomplete"},

                "Mary": {
                "makeup" : 0,
                "jewelry" : 0,
                "weights" : 0,
                "budget" : 100,
                "status" : "incomplete"},

                "Fiona": {
                "flag" : 0,
                "paint" : 0,
                "clothes" : 0,
                "budget" : 60,
                "status" : "incomplete"},

                "Allen": {
                "lights" : 0,
                "headphones" : 0,
                "gaming console" : 0,
                "budget" : 120,
                "status" : "incomplete"}
                }

x = 'n'
choice = ""
print("")
print("Welcome to my Shopping List App! Here you can update the price of items for each")
print("person and see whether or not you've gone over/under their budget.")
print("")

def displayMenu():
    print("-------------------------------------")
    print("Menu:")
    print("-------------------------------------")
    print("Update Shopping List - (Type U)")
    print("Complete Shopping List - (Type C)")
    print("Display Shopping List - (Type D)")
    print("Exit Application - (Type E)")
    print("-------------------------------------")

def getChoice():
    #Decides input value
    global choice
    displayMenu()
    choice = str(input("What would you like to do? "))
    return choice

def completeShoppingList():
    x = 'n'
    while x == 'n':
        print("----------")
        #Prints each persons name in seperate lines (They're status cannot equal "complete")
        for person in shoppingList:
            if shoppingList[person]["status"] != 'complete':
                print(person)
        print("----------")
        name = str(input("Who would you like to update? "))
        #Makes sure the user doesn't input a complete person's name
        if name in shoppingList and shoppingList[name]["status"] != 'complete':
            shoppingList[name]["status"] = "complete"
            #Prints everything but the selected persons status
            for item, amount in shoppingList[name].items():
                if item == "status":
                    print(name + "'s status is now", "'" + amount + "'")
            x = str(input("Are you done updating the customers (y/n)? ")) 
        else:
            print("That is not a valid name. Please select a valid name to complete. ")

def updateShoppingList():
    x = 'n'
    while x == 'n':
        print("----------")
        #Prints each persons name in seperate lines (They're status cannot equal "complete")
        for person in shoppingList:
            if shoppingList[person]["status"] != 'complete':
                print(person)
        print("----------")
        command = str(input("Which persons items would you like to view? "))
        #Prints all of the items, excluding the status and the budget
        if command in shoppingList and shoppingList[command]["status"] != 'complete':
            for item, amount in shoppingList[command].items():
                if item != "budget" and item != "status":
                    print(item, ':', round(amount, 2))
            choice = str(input("Which item would you like to update the price of? "))
            #Makes sure the users input is in the shoppingList
            if choice in shoppingList[command]:
                if choice != "budget" and choice != "status":
                    priceChange = float(input("What is the value of this item? "))
                    print("-----------------")
                    shoppingList[command][choice] = priceChange
                    for item, amount in shoppingList[command].items():
                        if item != "status":
                            #Rounds the value if the user inputs a too long number
                            print(item, ':', round(amount, 2))
                    x = str(input("Are you done updating (y/n)? "))
            else:
                print("That is not an item.")
        else:
            print("That is not a person.")

def displayShoppingList():
    #total amount of all people
    total = 0
    print("---------------------------------")
    print("Shopping List:")
    for person, value in shoppingList.items():
        totalSpent = 0
        totalOverUnder = 0
        print(person, '=')
        for item, amount in value.items():
            print(item, ':', amount)
        for item in shoppingList[person]:
            if item != "budget" and item != "status":
                #adds the values to toal and totalSpent
                totalSpent = totalSpent + round(float(shoppingList[person][item]), 2)
                total = total + round(float(shoppingList[person][item]), 2)
        print("------------------------")
        print("Budget Amount:", shoppingList[person]["budget"])
        print("Under/Over budget:", round(shoppingList[person]["budget"] - totalSpent, 2))
        print("Total Spent:", round(totalSpent, 2))
        print("------------------------")
        print("---------------------------------")
    print("You have spent a total of $" + str(total))

def exitApplication():
    print("Thank you for using this application. Good Bye.")

while x =="n": 
    getChoice()
    if choice == "U":
        updateShoppingList()
    elif choice == "C":
        completeShoppingList()
    elif choice == "D":
        displayShoppingList()
    elif choice == "E":
        x = "bhp"
        exitApplication()
    else:
        print("That is not a value")
