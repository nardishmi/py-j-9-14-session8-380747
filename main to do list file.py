

from functionstodolist import *
while True:
    menu = input(" 1.Add New Task 2.Show All Tasks 3.Complete Task 4.Delete Task 5.Search Task 6.Show Pending Tasks 7.Edit Task 8.Show Statistics 9.Exit:")
    while True:
        match menu:
            case "1":
                add_task()
            case "2":
                show_tasks()
            case "3":
                complete_task()
            case "4":
                delete_task()
            case "5":
                search_task()
            case "6":
                show_pending_tasks()
            case "7":
                edit_task()
            case "8":
                show_statistics()
            case "9":
                print("Exit")
                break
            case _:
                print("wrong option!")
                

