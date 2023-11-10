# Creating the dictionary for Food Truct Menu 
menu = {
    "Pizza": {
        "Pepperoni (Slice)": 3.99,
        "Cheese (Slice)": 3.99,
        "Gluten Free": 13.99,
        "Deluxe Pizza": 13.99
    },
    "Speciality Dogs": {
        "Chicago": 4.49,
        "The Old Faithful": 4.49,
        "The Chilli Dog": 4.99,
        "The Real Man Thai": 5.59,
    },
    "Drinks": {
        "Bottled Water": {
            "Aquafina": 1.49,
            "Dasani": 1.79,
            "Fiji Water": 1.99
        },
        "Coffee": {
            "Cappuccino": 3.49,
            "Flat White": 3.39,
            "Americao": 3.99
        },
        "Fruite Juices": {
            "Pineapple": 3.5,
            "Orange": 2.5,
            "Apple": 2.5
        }
    },
    "Burger & Sandwiches": {
        "Aloha Chicken": 6.99,
        "Burger": {
            "Farmers Burger": 4.49,
            "BYOBB": 4.99
        },
        "BBQ Pulled Pork Pavlova": 6.99,
        "Chop House Club pudding": 7.49,
        "Philly Chessesteak": 7.99
    }
}

# Empty list Initialization - store the final output of orders
order_list = {
    "Item name":[],
    "Price":[],
    "Quantity":[]
}
 
# Initialize empty list to store user input 
menu_selection = {}

# Launch the Food Truck & present a greeting to the customer
print("Welcome to Arnab's food truck at you favourite Dublin Downtown")

# Creating a continuous loop for multiple iteration for Customers choices
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? If you do not wish to proceed, hit Enter")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type a menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}!")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
            menu_selection = input("Type the item number for your selection: ")
           
                    
            # 3. Check if the customer typed a number
            if menu_selection.isdigit():

                # Convert the menu selection to an integer
                int(menu_selection)
              #  print("you have selected: " + menu_selection)
                #print(menu_items.keys())
                #print(f'{menu_items[int(menu_selection)]}')
                
                # 4. Check if the menu selection is in the menu items
                sub_menu_item_number_list = list(menu_items.keys())
               # print (sub_menu_item_number_list)
                
                if int(menu_selection) in sub_menu_item_number_list:
                    #print("You have made a valid selection!")
                
                    
                    # Store the item name as a variable

                    cust_order = menu_items[int(menu_selection)]
                   # print (cust_order)

                    selected_item_name = cust_order.get("Item name")

                    selected_item_price = cust_order.get("Price")

                    print("You have selected:", selected_item_name, "for", selected_item_price, "each")
                    #Find out how to store only the item name later
                  
                    
                    # Ask the customer for the quantity of the menu item
                    order_quantity = input(f"How many {selected_item_name} do you want to order? If quantity is invalid, it will be defaulted to 1!  ")
                    

                    # Check if the quantity is a number, default to 1 if not                    
                    try:
                        order_quantity = int(order_quantity)
                    except ValueError:
                        order_quantity = 1
                    
                  #  print("You selected: ", order_quantity , "items of " , cust_order )




                    # Add the item name, price, and quantity to the order list
                    order_list["Item name"].append(selected_item_name)
                    order_list["Price"].append(float(selected_item_price))
                    order_list["Quantity"].append(int(order_quantity))

                    print ("Your current order is: ", order_list)

                    # Tell the customer that their input isn't valid
                    

                else: 
                    print ("Item",menu_selection, "does not exist") 


                # Tell the customer they didn't select a menu option
            else:
                print("You didn't select a valid item number.")

        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} is not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")
        # 5. Check the customer's input
        match (keep_ordering.lower()):
                # Keep ordering
            case 'y':
                place_order = True
                print("What would you like to order next?")
                keep_ordering
            
                # Since the customer decided to stop ordering, thank them for
                # their order
            case 'n':
                place_order = False
                print("Thank you for your order.")
                break
                 
            case _ :
                place_order = False
                print("Would you like to order more? You didn't select Y/N as an option. The program will end")
                print("Restart program to order")
                StopIteration()
        
                # Complete the order
            
 
                # Exit the keep ordering question loop


                # Tell the customer to try again
                print("Please try again")

# Print out the customer's order
print("This is what we are preparing for you.\n")
menu_selection
# Uncomment the following line to check the structure of the order
#print(order)


print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order
#for k, v in order_list.items():



    # 7. Store the dictionary items as variables
order_itm_ary = order_list.get("Item name")
order_prc_ary = order_list.get("Price")
order_qty_ary = order_list.get("Quantity")
    #order_amt_ary = (order_prc) * (order_qty)
length = len(order_itm_ary)
total_order = 0.00

item_space = 26
price_space = 8
quantity_space = 10


for m in range(length):
    order_amt = order_prc_ary[m] * order_qty_ary[m]
    


    # 8. Calculate the number of spaces for formatted printing
    itm = item_space - len(order_itm_ary[m]) - 2
    prc = price_space - len(str(order_prc_ary[m])) - 3
    qty = quantity_space - len(str(order_qty_ary[m]))



    # 9. Create space strings
    total_order = total_order + order_amt



    # 10. Print the item name, price, and quantity
    print(order_itm_ary[m],itm * " ", "|", order_prc_ary[m],prc * " ", "|", order_qty_ary[m],qty * " ", " = ", order_amt)



# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
print("\nYour total order amount is: $", round(total_order,2))
print("Thank you for shopping with us!!!\n")