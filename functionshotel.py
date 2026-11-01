


rooms = [[101, "Single", 1, 50, False],
    [102, "Double", 2, 80, False],
    [103, "Suite", 4, 150, False],
    [104, "Single", 1, 50, False],
    [105, "Double", 2, 80, False],
    [106, "Suite", 4, 150, False]]
reservations = []
def show_all_rooms():
    global rooms
    for room in rooms:
        if room[4] == True:
            status = "Reserved"
        else:
            status = "Available"
        print("Room Number:", room[0])
        print("Room Type:", room[1])
        print("Capacity:", room[2])
        print("Price:", room[3], "$")
        print("Status:", status)
def show_available_rooms():
    global rooms
    found = False
    for room in rooms:
        if room[4] == False:
            print("Room Number:", room[0])
            print("Room Type:", room[1])
            print("Capacity:", room[2])
            print("Price:", room[3], "$")
            print("Status: Available")
            found = True
    if found == False:
        print("No available rooms!")
def reserve_room():
    global rooms
    global reservations
    name = input("Enter full name: ").strip()
    phone = input("Enter phone number: ").strip()
    if name == "" or phone == "":
        print("Name and phone cannot be empty!")
        return
    if not phone.isdigit():
        print("Invalid phone number!")
        return
    room_number = input("Enter room number: ")
    if not room_number.isdigit():
        print("Invalid room number!")
        return
    room_number = int(room_number)
    found = False
    for room in rooms:
        if room[0] == room_number:
            found = True
            if room[4] == True:
                print("Room is already reserved!")
                return
            people = input("Number of people: ")
            nights = input("Number of nights: ")
            if not people.isdigit() or not nights.isdigit():
                print("Please enter valid numbers!")
                return
            people = int(people)
            nights = int(nights)
            if people <= 0 or nights <= 0:
                print("People and nights must be greater than zero!")
                return
            if people > room[2]:
                print("Number of people exceeds room capacity!")
                return
            total_price = room[3] * nights
            reservation = [name,phone,room_number,people,nights,total_price]
            reservations.append(reservation)
            room[4] = True
            print("Reservation completed successfully!")
            print("Total Price:", total_price, "$")
            return
    if found == False:
        print("Room does not exist!")
def cancel_reservation():
    global rooms
    global reservations
    if len(reservations) == 0:
        print("No reservations found!")
        return
    room_number = input("Enter room number: ")
    if room_number.isdigit():
        room_number = int(room_number)
        found = False
        for reservation in reservations:
            if reservation[2] == room_number:
                found = True
                print("Customer:", reservation[0])
                print("Room:", reservation[2])
                confirm = input("Are you sure? (yes/no): ").lower()
                if confirm == "yes":
                    reservations.remove(reservation)
                    for room in rooms:
                        if room[0] == room_number:
                            room[4] = False
                    print("Reservation cancelled!")
                else:
                    print("Cancellation stopped!")
                return
        if found == False:
            print("Reservation not found!")
    else:
        print("Invalid room number!")
def search_reservation():
    global reservations
    if len(reservations) == 0:
        print("No reservations found!")
        return
    search = input("Enter name, phone or room number: ").lower().strip()
    if search == "":
        print("Search cannot be empty!")
        return
    found = False
    for reservation in reservations:
        if (search in reservation[0].lower()
            or search in reservation[1]
            or search == str(reservation[2])):
            print("Customer:", reservation[0])
            print("Phone:", reservation[1])
            print("Room:", reservation[2])
            print("People:", reservation[3])
            print("Nights:", reservation[4])
            print("Total Price:", reservation[5], "$")
            found = True
    if found == False:
        print("Reservation not found!")
def calculate_price():
    global rooms
    global reservations
    if len(reservations) == 0:
        print("No reservations found!")
        return
    room_number = input("Enter room number: ")
    if room_number.isdigit():
        room_number = int(room_number)
        for reservation in reservations:
            if reservation[2] == room_number:
                for room in rooms:
                    if room[0] == room_number:
                        total = room[3] * reservation[4]
                        print("Room Price:", room[3], "$")
                        print("Number Of Nights:", reservation[4])
                        print("Total Price:", total, "$")
                        return
        print("Reservation not found!")
    else:
        print("Invalid room number!")
# 7. Show All Reservations
def show_all_reservations():
    global reservations
    if len(reservations) == 0:
        print("No reservations found!")
        return
    for i, reservation in enumerate(reservations, start=1):
        print("Reservation Number:", i)
        print("Customer:", reservation[0])
        print("Phone:", reservation[1])
        print("Room Number:", reservation[2])
        print("Number Of People:", reservation[3])
        print("Number Of Nights:", reservation[4])
        print("Total Price:", reservation[5], "$")
def hotel_statistics():
    global rooms
    global reservations
    total_rooms = len(rooms)
    reserved_rooms = 0
    available_rooms = 0
    total_income = 0
    for room in rooms:
        if room[4] == True:
            reserved_rooms += 1
        else:
            available_rooms += 1
    for reservation in reservations:
        total_income += reservation[5]
    if total_rooms > 0:
        occupancy = (reserved_rooms / total_rooms) * 100
    else:
        occupancy = 0
    print("Total Rooms:", total_rooms)
    print("Reserved Rooms:", reserved_rooms)
    print("Available Rooms:", available_rooms)
    print("Total Income:", total_income, "$")
    print("Occupancy Rate:", occupancy, "%")
    