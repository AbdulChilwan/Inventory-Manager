# Creating a 'shoe' class, to save data from the inventory file as an object of type shoe.
class Shoes():
    # Constructor for shoe data
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        
    # Defining class method, to get the cost
    def get_cost(self):
        return self.cost
    
     # Defining class method, to get the quantity
    def get_quantity(self):
        return self.quantity
    
     # Defining class method, to get the shoe information
    def __str__(self):
        return f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}"

# Function for read the data from inventory.txt and saving the info as shoe objects.
def read_shoes_data():
    # Try block, incase file does not open, or other errors occur
    try:
        with open('inventory.txt','r')as file:
            # Skipping the first line, as it is just headings.
            next(file)
            for line in file:
                # Removing empty lines and splitting by each ","
                line = line.strip('\n')
                line = line.split(",")
                # Adding the info as arguments. Referencing the index as each index is a different data.
                shoe_list.append(Shoes(line[0], line[1], line[2], line[3], line[4]))

    # Exceptions handled incase file error, or any other unexpected error.
    except FileNotFoundError:
        print("This file was not found.")
    except Exception:
        print("An error has occured trying to read the data of this file.")
    finally:
        file.close()

# Function for adding a new shoe to the list of objects.
def capture_shoes():
    print("Please enter the following information")
    print("--------------------------------------------")
    # Asking user to prompt data
    country = input("Country this shoe is from: ")
    code = input("Code of this shoe: ")
    product = input("Name of this shoe: ")
    cost = input("Cost of this shoe: ")
    quantity = input("How many quantity is available: ")
    print("--------------------------------------------")
    # Adding the data to the list of shoe objects.
    shoe_list.append(Shoes(country, code, product, cost, quantity))
    print("Thank you, the data has been saved as an object, and saved to the list.")

# Creating a function to view all shoe ojects.
def view_all():
    # Using a for loop and referencing the shoe objects by index, and calling the class function to view the details.
    for i in range (len(shoe_list)):
        print(shoe_list[i].__str__())
        
    # if the list is empty, an error message shall be prompted.
    if len(shoe_list) == 0:
        print("List is empty, please read data from the file, or enter data manuelly first.")
        
# Function for adding stock to the lowest quantity item.
def re_stock():
    # Creating a temp new list.
    new_shoe_list = []
    
    try:
         # If list of objects are empty, exception will be promt
        if (len(shoe_list) == 0):
            raise Exception
        
        '''
        Searching for lowest quantity item, deleting all the others till lowest is found,
        and adding the deleted into a temp new list. 
        '''
        for i in range (len(shoe_list)):
            if len(shoe_list) == 1:
                break
            elif int(shoe_list[0].quantity) > int(shoe_list[1].quantity):
                new_shoe_list.append(shoe_list[0])
                del shoe_list[0]

            elif int(shoe_list[0].quantity) < int(shoe_list[1].quantity):
                new_shoe_list.append(shoe_list[1])
                del shoe_list[1]

        # Displaying the lowest quantity item, asking the user if they want to add stock, 
        print("-----------------")
        print("Lowest quantity")      
        print(shoe_list[0].__str__())
        print("-----------------")
        answer = input("Would you like to add to this stock? ").casefold()
        # If yes, then asking to increase it by which amount and adding it to the current stock.
        if answer == 'yes'.casefold():
            add_stock = int(input("Enter how many stock you would like to add to the quantity: "))
            old = int(shoe_list[0].quantity)
            shoe_list[0].quantity = old + add_stock
            print('-------------')

            # Now adding the new list into the old list, this time the old list will have the updated data.
            for i in range (len(new_shoe_list)):
                shoe_list.append(new_shoe_list[i])

            # Writing the new list object to the file.        
            with open('inventory.txt','w') as file:
                file.write("Country,Code,Product,Cost,Quantity\n")
                for i in range (len(shoe_list)):
                    file.write(f'{shoe_list[i].__str__()}\n')

            print('Item is restocked, and updated on file.')
    # Exception is handled if the list of objects are empty
    except Exception:
        print("Sorry, file is empty, read the data first")

# Function for searching shoe by code.
def search_shoe():
    found_item = ""
    # Asking user to enter the code, then searches the objects based on the code.
    search_code = input("Insert the code of the shoe you looking for: ")
    for i in range (len(shoe_list)):
        if shoe_list[i].code == search_code:
            # If found, prints searched object's details
            print("Item found:")
            found_item = shoe_list[i]
            print (shoe_list[i].__str__())
    # If not found, error message promt.
    if found_item == "":
        print("No item of that code is on the list")

'''
Function for calculating all the stock value.
uses a for loop and multiplies the cost by quantity for each item. And displays each objects worth.
'''
def value_per_item():
    if len(shoe_list) == 0:
        print("List is empty, please read data from the file, or enter data manuelly first.")
    for i in range (len(shoe_list)):
        value = int(shoe_list[i].cost) * int(shoe_list[i].quantity)
        print (f"The total value for {shoe_list[i].product}, code ({shoe_list[i].code}) is : R{value}")
     
"""
 Function for searching the highest quantity of shoes object.
 Very similiar to the re stock function, except here we searching for the quantity.
 Then taking that hightest quantity object and displaying it's name to be on sale.
"""
def highest_qty():
    new_shoe_list = []
    try:
        if (len(shoe_list) == 0):
            raise Exception

        for i in range (len(shoe_list)):
            if len(shoe_list) == 1:
                break
            elif int(shoe_list[0].quantity) > int(shoe_list[1].quantity):
                new_shoe_list.append(shoe_list[1])
                del shoe_list[1]

            elif int(shoe_list[0].quantity) < int(shoe_list[1].quantity):
                new_shoe_list.append(shoe_list[0])
                del shoe_list[0]

        print("The below shoe is on sale !")      
        print(shoe_list[0].product)

        new_shoe_list.append(shoe_list[0]) # now all are in the list

        for i in range (len(new_shoe_list)):
            shoe_list.append( new_shoe_list[i])
                

    except Exception:
        print("Sorry, file is empty, read the data first")



def main():
    # Displaying the data in a uer friendly format. Asking the user which commands to execute.
    print("---------------- Welcome to the stock inventory system ----------------")
    option = True

    while option:
        print("1 : Read data from inventory file \n2 : Add new shoe data \n3 : view all data")
        print("4 : Restock lowest quantity item \n5 : Search for a specific shoe \n6 : Total worth of stock available")
        print("7 : Highest quantity item \n0 : Exit program")
        print("============================================")
        user_input = input("Please enter your choice: ")
        print("------------------------------------------------------------------------")

        if user_input == "1":
            read_shoes_data.shoe_list = []
            read_shoes_data()
            print("Data has been read and saved")
            print("------------------------------------------------------------------------")

        elif user_input == "2":
            capture_shoes()
            print("------------------------------------------------------------------------")

        elif user_input == "3":
            view_all()
            print("------------------------------------------------------------------------")

        elif user_input == "4":
            re_stock()
            print("------------------------------------------------------------------------")

        elif user_input == "5":
            search_shoe()
            print("------------------------------------------------------------------------")

        elif user_input == "6":
            value_per_item()
            print("------------------------------------------------------------------------")

        elif user_input == "7":
            highest_qty()
            print("------------------------------------------------------------------------")

        elif user_input == "0":
            option = False
            print("### Good Bye ###")

        else:
            print("------------------------------------------------------------------------")
            print("Please enter a digit corresponding to the operation you wish to execute.")
            print("------------------------------------------------------------------------")

# Running the main function
shoe_list = []
main()
