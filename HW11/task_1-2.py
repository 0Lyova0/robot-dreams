# Unfortunately my homework 7 is not done, so I take some part of them
# I cant find the right solution (((


contacts = {"Bob": 1234}

def new(contacts):
    print("Enter name: ")
    name = input("")
    print("enter last name: ")
    last_name = input("")
    print("enter phone_number: ")
    phone_number = input("")
    new_contact = {
        "name": name,
        "last_name": last_name,
        "phone_number": phone_number,
    }
    contacts.append(new_contact)
    print("Contact saved")


def delete(contacts):
    print("Enter name to delete: ")
    del_name = input("")
    for contact in contacts:
        if contact[name] == del_name:
            print("Are You shore? Yes or No?: ")
        confirmation = input("")
        if confirmation == "Yes":
            contact.remove(contact)
            print("Contact was deleted")


print("Welkome to your phone book.")
print('choose \n'
      '"new" - to greate a contact \n'
      '"del" - to delete contact: \n'
      '"exit" - to exit')

while True:
    print("Enter command: ")
    command = input(" > ")
    if command == "new":
        new(contacts)
    if command == "del":
        delete(contacts)
    if command == "exit":
        break
    else:
        print("Unknown command")



try:
    value = delLete
except NameError:
    print ("A Name Error occurred")


import time

counter = 7
while counter:
    name = input("Enter a name: ")
    try:
        print(contacts[name])
    except KeyError:
        print("Name which you entered does not exist")
    finally:
        time.sleep(2)
        counter -= 1



# TEST TODO find out all exceptions
try:
    print(1/0)
except Exception as e:
    print(type(e), e)



#  ===== task_2 =====

class MyCustomException(Exception):
    pass

try:
    raise MyCustomException("Just a test")
except MyCustomException:
    print("Custom exception is occurred")