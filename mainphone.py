

from functionsphone import *
while True:
    menu=input("1.Add Contact 2.Show All Contacts 3.Search Contact 4.Edit Contact 5.Delete Contact 6.Count Contacts 7.Exit:")
    while True:
        match menu:
            case "1":
                add_contact()
            case "2":
                show_contacts()
            case "3":
                search_contact()
            case "4":
                edit_contact()
            case "5":
                delete_contact()
            case "6":
                count_contacts()
            case "7":
                print("Goodbye!")
                break
            case _:
                print("Invalid choice!")
