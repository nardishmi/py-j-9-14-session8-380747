

tasks = []
def add_task():
    """
    Add a new task

    Args:
        No arguments

    Returns:
        None
    """
    global tasks

    title = input("activity name: ").strip()
    if title == "":
        print(" it can't be empty!")
    else:
        duplicate = False
        for i in tasks:
            if i[0].lower() == title.lower():
                duplicate = True
        if duplicate:
            print("already done!")
        else:
            description = input("description: ").strip()
            if description == "":
                print("it can't be empty!")
            else:
                tasks.append([title, description, False])
                print("done!")
def show_tasks():
    """
    Show all tasks

    Args:
        No arguments

    Returns:
        None
    """
    global tasks

    if not tasks:
        print("there isn't any task!")
    else:
        for i, t in enumerate(tasks, start=1):
            if t[2] == True:
                status = "Completed"
            else:
                status = "Pending"
            print("number:", i)
            print("name:", t[0])
            print("description:", t[1])
            print("status:", status)
def complete_task():
    """
    Complete a task

    Args:
        No arguments

    Returns:
        None
    """
    global tasks

    if not tasks:
        print("list is empty!")
    else:
        show_tasks()
        number = input("activity number: ")
        if number.isdigit():
            number = int(number)
            if 1 <= number <= len(tasks):
                if tasks[number - 1][2] == True:
                    print("already done!")
                else:
                    tasks[number - 1][2] = True
                    print("done!")
            else:
                print("number is wrong!")
        else:
            print("pls add number .")
def delete_task():
    """
    Delete a task

    Args:
        No arguments

    Returns:
        None
    """
    global tasks

    if not tasks:
        print("list is empty!")
    else:
        show_tasks()
        number = input("activity number for deleting: ")
        if number.isdigit():
            number = int(number)
            if 1 <= number <= len(tasks):
                tasks.pop(number - 1)
                print("activity deleted !")
            else:
                print("number is wrong!")
        else:
            print("pls add number!")
def search_task():
    """
    Search tasks by title or description

    Args:
        No arguments

    Returns:
        None
    """
    global tasks

    if not tasks:
        print("list is empty!")
    else:
        search = input("word: ").lower().strip()
        if search == "":
            print("found word is empty!")
        else:
            found = False
            for i, t in enumerate(tasks, start=1):
                if search in t[0].lower() or search in t[1].lower():
                    print("number:", i)
                    print("name:", t[0])
                    print("description:", t[1])
                    if t[2] == True:
                        print("status: Completed")
                    else:
                        print("status: Pending")
                    found = True
            if found == False:
                print("activity not founded !")
def show_pending_tasks():
    """
    Show unfinished tasks

    Args:
        No arguments

    Returns:
        None
    """
    global tasks

    found = False
    for i, t in enumerate(tasks, start=1):
        if t[2] == False:
            print("number:", i)
            print("name:", t[0])
            print("descriotion:", t[1])
            print("status: Pending")
            found = True
    if found == False:
        print("activity dosn't exist!")
def edit_task():
    """
    Edit task title and description

    Args:

        No arguments

    Returns:

        None
    """
    global tasks

    if not tasks:
        print("list is empty!")
    else:
        show_tasks()
        number = input("activity number for edit : ")
        if number.isdigit():
            number = int(number)
            if 1 <= number <= len(tasks):
                new_title = input("new name: ").strip()
                if new_title == "":
                    print("name is empty!")
                else:
                    duplicate = False
                    for i, t in enumerate(tasks):
                        if i != number - 1:
                            if t[0].lower() == new_title.lower():
                                duplicate = True
                    if duplicate:
                        print("the name is already exists!")
                    else:
                        new_description = input("new discription: ").strip()
                        if new_description == "":
                            print("dicription is empty!")
                        else:
                            tasks[number - 1][0] = new_title
                            tasks[number - 1][1] = new_description
                            print("activity edited!")
            else:
                print("number is wrong!")
        else:
            print("enter number!")
def show_statistics():
    """
    Show task statistics

    Args:

        No arguments

    Returns:

        None

    """
    global tasks

    total = len(tasks)
    completed = 0
    pending = 0
    for t in tasks:
        if t[2] == True:
            completed += 1
        else:
            pending += 1
    print("total activities:", total)
    print("completed activitys:", completed)
    print("completed activitys:", pending)
    