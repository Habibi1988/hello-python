users = [
    {'name': 'john', 'phone': '603555555', 'age': 55},
    {'name': 'Michel', 'phone': '603558755', 'age': 55},
        {'name': 'dani', 'phone': '603555545', 'age': 26}
]

# Append a new dictionary to the list
users.append({'name': 'david', 'phone': '118', 'age': 55})

# Print the updated list
print(users)

print(type(users))
for user in users:
    print (user ['age'])


# Get user input for the new user
name = input("Enter name: Mustafa ")
phone = input("Enter phone: 88")
age = int(input("Enter age: 77"))
 
