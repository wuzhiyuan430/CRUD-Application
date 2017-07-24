import csv

products = []

products_csv = "data/products.csv"
headers = ["id", "name", "aisle", "department", "price"] # for "Further Exploration" use: ["product_id", "product_name", "aisle_id", "aisle_name", "department_id", "department_name", "price"]
user_input_headers = [header for header in headers if header != "id"] # don't prompt the user for the product_id

def get_product_id(product): return int(product["id"])

def auto_incremented_id():
    product_ids = map(get_product_id, products)
    return max(product_ids) + 1

#
# READ PRODUCTS FROM FILE
#

with open(products_csv, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for ordered_dict in reader:
        products.append(dict(ordered_dict))

#
# HANDLE USER INPUT
#

def list_products():
    print("LISTING PRODUCTS HERE")
    for product in products:
        print(" + Product #" + str(product["id"]) + ": " + product["name"])

def show_product():
    product_id = input("OK. WHAT IS THE PRODUCT'S ID? ")
    product = [p for p in products if p["id"] == product_id][0]
    if product:
        print("READING PRODUCT HERE", product)
    else:
        print("COULDN'T FIND A PRODUCT WITH IDENTIFIER", product)

def create_product():
    print("OK. PLEASE PROVIDE THE PRODUCT'S INFORMATION...")
    product = {"id": auto_incremented_id() }
    for header in user_input_headers:
        product[header] = input("The '{0}' is: ".format(header))
    products.append(product)
    print("CREATING PRODUCT HERE", product)

#def update_product():
#    product_id = input("OK. WHAT IS THE PRODUCT'S ID? ")
#    product = [p for p in products if p["id"] == product_id][0]
#    if product:
#        print("OK. PLEASE PROVIDE THE PRODUCT'S INFORMATION...")
#        for header in user_input_headers:
#            product[header] = input("Change '{0}' from '{1}' to: ".format(header, product[header]))
#        print("UPDATING PRODUCT HERE", product)
#    else:
#        print("COULDN'T FIND A PRODUCT WITH IDENTIFIER", product_id)


def update_product():
    print("UPDATING A PRODUCT")
    choose_a_product = input("OK. Please specify the product's identifier: ")
    print("OK. Please specify the product's information..." )
    product = [p for p in products if p["id"] == choose_a_product][0]
    print(product)
    product["name"] = input("Change name from {0} to: " .format(product["name"]))
    product["aisle"] = input("Change aisle from {0} to: " .format(product["aisle"]))
    product["department"] = input("Change department from {0} to: " .format(product["department"]))
    product["price"] = input("Change price from {0} to: " .format(product["price"]))
#    changed_name = input("Change name from {0} to: " .format(product["name"]))
#    changed_aisle = input("Change aisle from {0} to: " .format(product["aisle"]))
#    changed_department = input("Change department from {0} to: " .format(product["department"]))
#    changed_price = input("Change price from {0} to: " .format(product["price"]))
#    updated_product = {}
#    updated_product = {"id": str(product["id"]), "name": changed_name, "aisle": changed_aisle, "department": changed_department, "price": changed_price}
#    product = updated_product

    print("UPDATING A PRODUCT HERE!", product)

def destroy_product():
    product_id = input("OK. WHAT IS THE PRODUCT'S ID? ")
    product = [p for p in products if p["id"] == product_id][0]
    if product:
        print("DESTROYING PRODUCT HERE", product)
        del products[products.index(product)]
    else:
        print("COULDN'T FIND A PRODUCT WITH IDENTIFIER", product_id)

menu = """
-----------------------------------
PRODUCTS APPLICATION
-----------------------------------
Welcome {0}!
There are {1} products in the database.
    operation | description
    --------- | ------------------
    'List'    | Display a list of product identifiers and names.
    'Show'    | Show information about a product.
    'Create'  | Add a new product.
    'Update'  | Edit an existing product.
    'Destroy' | Delete an existing product.
Please select an operation: """.format("@5zy shore", len(products)) # end of multi- line string. also using string interpolation

crud_operation = input(menu)

if crud_operation.title() == "List":
    list_products()
elif crud_operation.title() == "Show":
    show_product()
elif crud_operation.title() == "Create":
    create_product()
elif crud_operation.title() == "Update":
    update_product()
elif crud_operation.title() == "Destroy":
    destroy_product()
else:
    print("OOPS SORRY. PLEASE TRY AGAIN.")

#
# WRITE PRODUCTS TO FILE
#

with open(products_csv, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=headers)
    writer.writeheader()
    for product in products:
        writer.writerow(product)

# don't run this app unless this script is executed from the command line.
# this strategy allows us to test the app
#if __name__ == "__main__":
#    run()
