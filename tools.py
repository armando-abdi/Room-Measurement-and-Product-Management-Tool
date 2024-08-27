#This function is to insert the length and width to calculate:
#the total sq ft area of a room's measures.
#also checks wether or not if an input is valid.
#If not, it is going to keep asking the user for a valid input.

def sq_ft_area():
    while True:
        try:
            length = float(input('Enter length: '))
            break
        except ValueError:
            print('Invalid input, please enter a number. #')
    while True:
        try:
            width = float(input('Enter width: '))
            break
        except ValueError:
            print('Invalid input, please enter a number. #')
    area = round(length * width, 2)
    return area

#This function code will ask the user if they want to calculate room's:
#measure as a question with Y/N then does a loop to check answer,
#to wether or not to execute the sq_ft_area() function.

def get_sq_ft_area():
    ask_to_get_sq_ft_area = input('Would you like to get the total sq ft area of a specific room? Y/N: ')
    
    while True:
        if ask_to_get_sq_ft_area.lower() == 'y':
            print("You chose 'Y'. Proceeding to get the total square footage.")
            print(sq_ft_area())
            
            
            while True:
                another_sq_ft_area = input('Would you like to get another sq ft area total? Y/N: ')
                
                if another_sq_ft_area.lower() == 'y':
                    print(sq_ft_area())
                      
                elif another_sq_ft_area.lower() == 'n':
                    print("You chose 'N'. Proceeding to exit.")
                    print('Exit confirmed')
                    main_tools_menu() # Print the main menu
                    return  # Exit outer loop function
                else:
                    print('Invalid input. Please enter Y or N:')
                    
        elif ask_to_get_sq_ft_area.lower() == 'n':
            print("You chose 'N'. Proceeding to exit.")
            print('Exit confirmed')
            main_tools_menu() # Print the main menu
            break
        else:
            ask_to_get_sq_ft_area = input('Invalid input. Please enter Y or N to proceed: ')

# Call the function directly without print


#This is going to be a system function which is going to be a list that takes in flooring and carpet products by inputs.
#For example it is going to take the product names, and sq ft coverage.

material_names = []
material_sq_ft_coverages = []

def products_management(material_names, material_sq_ft_coverages):
    ask_to_input_material = input('Please insert material name: ')
  
    while True: 
        if ask_to_input_material:
            ask_to_input_sq_ft_coverages = float(input('Please insert sq ft coverage for: ' + str(ask_to_input_material.title()) + ': '))
            material_names.append(ask_to_input_material.title())
            material_sq_ft_coverages.append(ask_to_input_sq_ft_coverages)
            converted_products_info = list(zip(material_names, material_sq_ft_coverages))
            print(converted_products_info)
            print('Exit confirmed')
            main_tools_menu()  # Print the main menu
            
            while True:
                ask_to_input_material_again = input('Would you like to insert another material name? Y/N: ').lower()
                if ask_to_input_material_again == 'y':
                    print("You chose 'Y'. Proceeding to insert another material name")
                    ask_to_input_material = input('Please insert material name: ')
                    ask_to_input_sq_ft_coverages = float(input('Please insert sq ft coverage for: ' + str(ask_to_input_material.title()) + ': '))
                    material_names.append(ask_to_input_material.title())
                    material_sq_ft_coverages.append(ask_to_input_sq_ft_coverages)
                    converted_products_info = list(zip(material_names, material_sq_ft_coverages))
                    print(converted_products_info)
                    print('Exit confirmed')
                    main_tools_menu() # Print the main menu
                elif ask_to_input_material_again == 'n':
                    print("You chose 'N'. Proceeding to exit")
                    print('Exit confirmed')
                    main_tools_menu()  # Print the main menu
                    return
                else:
                    print('Invalid input. Please enter Y or N:')
        else:
            break
    return material_names, material_sq_ft_coverages



#This function will serve as a way to modify your products names and sq ft area coverages,
#for each product like choose a product from the list and update it to a new one with also a new sq ft area coverage
#also this function will work together with: products_management function.

def product_management_update(material_names, material_sq_ft_coverages):
    # Combine material names and coverage into a list of tuples
    combined_converted_products_info = list(zip(material_names, material_sq_ft_coverages))
    print("Current Products:")
    for item in combined_converted_products_info:
        print(item)

    while True:
        ask_to_input_material_again = input('Do you want to update a product? (Y/N): ').strip().lower()
        
        if ask_to_input_material_again == 'y':
            update_product_name_find = input('Please enter the name of the product you want to update: ').title()
            
            # Find the index of the product to update
            for i, (name, coverage) in enumerate(combined_converted_products_info):
                if name == update_product_name_find:
                    print(f"Current details for {name}: Coverage = {coverage} sq ft")
                    
                    # Handle new name input
                    new_name = input('Enter the new material name: ').title()
                    
                    # Handle new coverage input with error handling
                    while True:
                        try:
                            new_coverage = float(input('Enter the new sq ft coverage: '))
                            break
                        except ValueError:
                            print("Invalid input. Please enter a numeric value for coverage.")
                    
                    # Update the product info
                    combined_converted_products_info[i] = (new_name, new_coverage)
                    print(f"Updated details: {combined_converted_products_info[i]}")
                    break
            else:
                print("Product not found.")
            
            # Print the updated list of products
            print("Updated Product List:")
            for item in combined_converted_products_info:
                print(item)
            print('Exit confirmed')
            main_tools_menu()  # Print the main menu
        
        elif ask_to_input_material_again == 'n':
            print("You chose 'N'. Proceeding to exit")
            # Print the final list of products
            print("Final list of products:")
            for item in combined_converted_products_info:
                print(item)
            print('Exit confirmed')
            main_tools_menu()  # Print the main menu
            break  # Exit the loop and end the function
        
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

    return combined_converted_products_info

# Assuming `material_names` and `material_sq_ft_coverages` are defined elsewhere in the code




# Main function menu for tool.
def main_tools_menu():
    
    print('Menu options:')
    print('1: Square Ft Area Calculator')
    print('2: Insert Product')
    print('3: Update A Product')
    
    while True:
        try:
            enter_option = int(input('Please insert an option: '))
            
            if enter_option == 1:
                get_sq_ft_area()
                break
            elif enter_option == 2:
                products_management(material_names, material_sq_ft_coverages)
                break
            elif enter_option == 3:
                updated_products = product_management_update(material_names, material_sq_ft_coverages)
                print(updated_products)
                break
            else:
                print('Invalid choice, please enter a number. 1, 2, or 3.')
        except ValueError:
            print('Invalid input, please enter a number. 1, 2, or 3.')

# Assuming you have defined material_names and material_sq_ft_coverages somewhere
# material_names = [...]
# material_sq_ft_coverages = [...]

main_tools_menu()