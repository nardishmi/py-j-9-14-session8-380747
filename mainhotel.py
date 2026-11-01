

from functionshotel import *

while True:
    menu = input(" 1.Show All Rooms 2.Show Available Rooms 3.Reserve Room 4.Cancel Reservation 5.Search Reservation 6.Calculate Price 7.Show All Reservations 8.Hotel Statistics 9.Exit:")
    while True:
        match menu:
            case "1":
                show_all_rooms()
            case "2":
                show_available_rooms()
            case "3":
                reserve_room()
            case "4":
                cancel_reservation()
            case "5":
                search_reservation()
            case "6":
                calculate_price()
            case "7":
                show_all_reservations()
            case "8":
                hotel_statistics()
            case "9":
                print("Thank you for using Hotel Reservation!")
                break
            case _:
                print("Invalid choice! Please try again.")
                