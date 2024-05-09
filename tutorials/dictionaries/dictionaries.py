customer = { # Dictionaries assign values to names and are definied with curly braces
    "name": "John Smith",
    "age": 30,
    "is_verified": True

}

customer["name"] = "Jack Smith"

print(customer)
print(customer["age"])
print(customer.get("email", "jacksmith@mail.com"))