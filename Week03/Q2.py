# Question 2: Shopping Cart (Lists - Searching and Removal)

cart = ["apple", "banana", "milk", "bread", "apple", "eggs"]
apple_count = cart.count("apple")
print("we have ", apple_count, "apples")
milk_position = cart.index("milk")
print("Posotion of milk ", cart.index("milk"))
cart.remove("apple")
print("Removed item using pop: ", cart.pop())
print("Is babana in the cart? " , "banana" in cart)
print("Final cart: ", cart)