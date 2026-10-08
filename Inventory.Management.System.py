# ================= INVENTORY MANAGEMENT SYSTEM ===================

class Product:
    def __init__(self, product_id, name, category, price, quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.product_id} - {self.name} - {self.category} - Rs. {self.price} - Qty: {self.quantity}"


class Inventory:
    def __init__(self):
        self.products = []
        self.filename = "products.txt"
        self.load_from_file()


    def add_product(self):
        product_id = input("Enter product id: ")
        name = input("Enter a name: ")
        category = input("Enter a category: ")
        price = int(input("Enter a price: "))
        quantity = int(input("Enter a quantity: "))

        product = Product(product_id,name,category,price,quantity)
        self.products.append(product)

    def view_products(self):
        if not self.products:
            print("No products available. ")

            return

        print("\n=========== All Products ============")

        for product in self.products:
            print(product)

    def search_product(self):
        product_id = input("Enter a product id to search: ")

        for product in self.products:
            if product.product_id == product_id:
                print(product)

                return
        print("Product not found. ")


    def update_product(self):
        product_id = input("Enter product id to update: ")

        for product in self.products:
            if product.product_id == product_id:
                product.product_id = input("Enter new product id: ")
                product.name = input("Enter new name: ")
                product.category = input("Enter new category: ")
                product.price = int(input("Enter new price: "))
                product.quantity = int(input("Enter new quantity: "))

                print("Product updated successfully.")
                return
            
        print("Product not found.")

    def delete_product(self):
        product_id = input("Enter product id to delete: ")

        for product in self.products:
            if product.product_id == product_id:
                self.products.remove(product)
                print("Product deleted successfully.")

                return

        print("Product not found.") 

    def update_stock(self):
        product_id = input("Enter product id: ")

        for product in self.products:
            if product.product_id == product_id:
                new_quantity = int(input("Enter new quantity: "))
                product.quantity = new_quantity

                print("Stock updated successfully.")
                return
            
        print("Product not found.")


    def low_stock_check(self):
        found = False

        for product in self.products:
            if product.quantity <= 5:
                print(product.product_id, "-", product.name, "- Low Stock")
                found = True

        if not found:
            print("No low stock products.")


    def total_inventory_value(self):
        total = 0

        for product in self.products:
            total += product.price * product.quantity

            print("Total Inventory Value:", total)

    def save_to_file(self):
        try:
            with open(self.filename, "w") as file:
                for product in self.products:
                    file.write(f"{product.product_id}|{product.name}|{product.category}|{product.price}|{product.quantity}\n")
            print("Products saved successfully.")

        except Exception as e:
            print("Error while saving:", e)


    def load_from_file(self):

        try:
            with open(self.filename, "r") as file:
                self.products = []
                for line in file:
                    line = line.strip()
                    if line:
                        data = line.split("|") 
                        product_id = data[0]
                        name = data[1]
                        category = data[2]
                        price = int(data[3])
                        quantity = int(data[4])

                        product = Product(product_id,name,category,price,quantity)
                        self.products.append(product)
                print("Products loaded successfully.")

         
        except FileNotFoundError:
            print("No saved file found.")


def main():

    inventory = Inventory()

    while True:
        print("\n=========== INVENTORY MANAGEMENT =============")
        print("1. Add Product")
        print("2. View Product")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Update Stock")
        print("7. Low stock check")
        print("8. Total Inventory Value")
        print("9. Save To File")
        print("10. Load From File")
        print("11. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            inventory.add_product() 

        elif  choice == "2":
            inventory.view_products()

        elif choice == "3":
            inventory.search_product()

        elif choice == "4":
            inventory.update_product()

        elif choice == "5":
            inventory.delete_product()

        elif choice == "6":
            inventory.update_stock()

        elif choice == "7":
            inventory.low_stock_check()

        elif choice == "8":
            inventory.total_inventory_value()

        elif choice == "9":
            inventory.save_to_file()

        elif choice == "10":
            inventory.load_from_file()

        elif choice == "11":
            print("Thank You! ")
            break

        else:
            print("Invalid Choice. ")

main() 


