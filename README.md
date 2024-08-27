# Room-Measurement-and-Product-Management-Tool

## Description
This is a beginner-level Python 3 project that calculates the total square footage area of a room based on user-provided length and width. The project also includes functionality to manage flooring and carpet products, including adding new products and updating existing ones.

## Table of Contents
- Features
- Functions
  - `sq_ft_area()`
  - `get_sq_ft_area()`
  - `products_management(material_names, material_sq_ft_coverages)`
  - `product_management_update(material_names, material_sq_ft_coverages)`
  - `main_tools_menu()`
- Usage
- Requirements
- License

## Features
- Calculate the total square footage area of a room.
- Validate user inputs to ensure they are numeric.
- Manage a list of flooring and carpet products, including their square footage coverage.
- Update product information.

## Functions

### `sq_ft_area()`
This function prompts the user to input the length and width of a room and calculates the total square footage area. It validates the inputs to ensure they are numeric.

### `get_sq_ft_area()`
This function asks the user if they want to calculate the square footage area of a room. If the user agrees, it calls the `sq_ft_area()` function. It also allows the user to calculate the area for multiple rooms.

### `products_management(material_names, material_sq_ft_coverages)`
This function manages a list of flooring and carpet products. It prompts the user to input the product name and its square footage coverage, and stores this information in lists. It also allows the user to add multiple products.

### `product_management_update(material_names, material_sq_ft_coverages)`
This function allows the user to update the information of existing products. It prompts the user to input the name of the product to be updated and the new information.

### `main_tools_menu()`
This function displays the main menu with options to calculate square footage, insert a product, or update a product. It calls the appropriate functions based on the user's choice.

## Usage
1. Run the script.
2. Follow the prompts to calculate the square footage area of a room or manage products.
3. Use the main menu to navigate between different functionalities.

## Requirements
- Python 3.x

## License
This project is the property of the sole proprietor, Armando Abdi.
