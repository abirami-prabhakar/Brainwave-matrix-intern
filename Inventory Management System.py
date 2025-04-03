import tkinter as tk
from tkinter import messagebox

# List to store products (for simplicity, using a list of dictionaries)
inventory = []

# Function to add product
def add_product():
    name = entry_name.get()
    quantity = entry_quantity.get()
    price = entry_price.get()

    # Data validation
    if not name or not quantity or not price:
        messagebox.showerror("Error", "Please fill in all fields.")
        return
    
    try:
        quantity = int(quantity)
        price = float(price)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for quantity and price.")
        return

    # Add product to inventory
    inventory.append({"name": name, "quantity": quantity, "price": price})
    messagebox.showinfo("Success", "Product added successfully.")
    show_products()

# Function to delete product
def delete_product():
    selected_item = listbox.curselection()
    if not selected_item:
        messagebox.showerror("Error", "Please select a product to delete.")
        return

    product_index = selected_item[0]
    inventory.pop(product_index)
    messagebox.showinfo("Success", "Product deleted successfully.")
    show_products()

# Function to show products in the listbox
def show_products():
    listbox.delete(0, tk.END)
    for product in inventory:
        listbox.insert(tk.END, f"{product['name']} | Quantity: {product['quantity']} | ${product['price']:.2f}")

# GUI Setup
root = tk.Tk()
root.title("Simple Inventory Management System")

# Input Fields
label_name = tk.Label(root, text="Product Name")
label_name.grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

label_quantity = tk.Label(root, text="Quantity")
label_quantity.grid(row=1, column=0)
entry_quantity = tk.Entry(root)
entry_quantity.grid(row=1, column=1)

label_price = tk.Label(root, text="Price")
label_price.grid(row=2, column=0)
entry_price = tk.Entry(root)
entry_price.grid(row=2, column=1)

# Buttons for actions
button_add = tk.Button(root, text="Add Product", command=add_product)
button_add.grid(row=3, column=0)

button_delete = tk.Button(root, text="Delete Product", command=delete_product)
button_delete.grid(row=3, column=1)

# Listbox to display products
listbox = tk.Listbox(root, height=10, width=50)
listbox.grid(row=4, column=0, columnspan=2)

# Load products into the listbox when the app starts
show_products()

# Run the application
root.mainloop()
