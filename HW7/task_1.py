

contacts = [
    {
        "name": "John",
        "last_name": "John",
        "phone": "123456"
    },
     {
        "name": "Bob",
        "last_name": "Test",
        "phone": "+1234"
    },
]

FORMAT_STR = "{:<15} {:<15} {:>12}"


def stats(contacts):
    print(len(contacts))

def list(contacts):
    print(FORMAT_STR.format("Name", "Last Name", 'Phone'))
    for contact in contacts:
        print(FORMAT_STR.format(
            contact["name"],
            contact["last_name"],
            contact["phone"]
        ))


def show (contacts):
    print("Enter Name:")
    name = input("> ")

    for contact in contacts:
        if contact["name"] == name:
            print(FORMAT_STR.format(
                contact["name"],
                contact["last_name"],
                contact["phone"]
            ))
            break
    else:
        print("Contact was not found")


def delete(contacts):
    print("Enter contact: ")
    name = input('> ')
    for contact in contacts:
        if contact["name"] == name:
            print("Do you want to delete a contact %s (yes/no)?: " % name)
            name_del = input('> ')
            if name_del == "yes":
                contacts.remove(contact)
                print("Contact was deleted %s " % name)


def add(contacts):
    print("Enter Name:")
    name = input("> ")
    print("Enter Last Name:")
    last_name = input("> ")
    print("Enter telephone number:")
    phone = input("> ")
    new_contact = {
        "name": name,
        "last_name": last_name,
        "phone": phone
    }
    contacts.append(new_contact)

    print("Contact was saved")


print("Welcome to the phone book.")
print("""Enter command:
* list - to view your contact list.
* show - find a contact by name
* stats - to show number of contacts
* add  - add contact
* del  - deleting a contact
* exit - for exit""")

while True:
    print("\nEnter command: ")
    command = input("> ")
    if command == "list":
        list(contacts)
    elif command == "show":
        show(contacts)
    elif command == "stats":
        stats(contacts)
    elif command == "add":
        add(contacts)
    elif command == "del":
        delete(contacts)
    elif command == "exit":
        break
    else:
        print("Unknown command")