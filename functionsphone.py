

contacts = []

def add_contact():
    global contacts
    name = input("Enter contact name: ").strip()
    if name == "":
        print("Name cannot be empty!")
        return
    phone = input("Enter phone number: ").strip()
    if len(phone) != 11 or not phone.startswith("09") or not phone.isdigit():
        print("Invalid phone number!")
        return
    for contact in contacts:
        if contact[1] == phone:
            print("This phone number already exists!")
            return
    contacts.append([name, phone])
    print("Contact added successfully!")
def show_contacts():
    global contacts
    if len(contacts) == 0:
        print("Contact list is empty!")
    else:
        print("ALL CONTACTS")
        for i in range(len(contacts)):
            print("Row:", i + 1)
            print("Name:", contacts[i][0])
            print("Phone:", contacts[i][1])
def search_contact():
    global contacts
    search = input("Enter name or phone number: ").strip()
    found = False
    for i in range(len(contacts)):
        if search.lower() in contacts[i][0].lower() or search in contacts[i][1]:
            print("Contact found!")
            print("Row:", i + 1)
            print("Name:", contacts[i][0])
            print("Phone:", contacts[i][1])
            found = True
    if found == False:
        print("Contact not found!")
def edit_contact():
    global contacts
    if len(contacts) == 0:
        print("Contact list is empty!")
        return
    show_contacts()
    row = input("Enter contact row number: ")
    if not row.isdigit():
        print("Invalid row number!")
        return
    row = int(row)
    if row < 1 or row > len(contacts):
        print("Contact not found!")
        return
    index = row - 1
    print("1. Edit Name")
    print("2. Edit Phone")
    print("3. Edit Both")
    choice = input("Choose: ")
    if choice == "1":
        new_name = input("Enter new name: ").strip()
        if new_name == "":
            print("Name cannot be empty!")
        else:
            contacts[index][0] = new_name
            print("Name updated successfully!")
    elif choice == "2" or choice == "3":
        new_phone = input("Enter new phone number: ").strip()
        if len(new_phone) != 11 or not new_phone.startswith("09") or not new_phone.isdigit():
            print("Invalid phone number!")
            return
        for i in range(len(contacts)):
            if i != index and contacts[i][1] == new_phone:
                print("This phone number already exists!")
                return
        if choice == "2":
            contacts[index][1] = new_phone
            print("Phone updated successfully!")
        else:
            new_name = input("Enter new name: ").strip()
            if new_name == "":
                print("Name cannot be empty!")
                return
            contacts[index][0] = new_name
            contacts[index][1] = new_phone
            print("Contact updated successfully!")
    else:
        print("Invalid choice!")
# 5. Delete Contact
def delete_contact():
    global contacts
    if len(contacts) == 0:
        print("Contact list is empty!")
        return
    show_contacts()
    row = input("Enter contact row number: ")
    if not row.isdigit():
        print("Invalid row number!")
        return
    row = int(row)
    if row < 1 or row > len(contacts):
        print("Contact not found!")
        return
    index = row - 1
    print("Selected Contact:")
    print("Name:", contacts[index][0])
    print("Phone:", contacts[index][1])
    confirm = input("Are you sure? (y/n): ").lower()
    if confirm == "y":
        contacts.pop(index)
        print("Contact deleted successfully!")
    else:
        print("Delete cancelled!")
def count_contacts():
    global contacts
    print("Total contacts:", len(contacts))
    