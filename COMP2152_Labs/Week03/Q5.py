# Question 5: Contact Book (Dictionaries - Basic Operations)
contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9999"
}

print(f"Alice's number: {contacts['Alice']}")
contacts["Diana"] = "555-4321"
print(f"Contacts after adding Diana: {contacts}")
contacts["Bob"] = "555-0000"
print(f"Contacts after updating Bob's number: {contacts}")
del contacts["Charlie"]
print(f"Contacts after removing Charlie: {contacts}")

