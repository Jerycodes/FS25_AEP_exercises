# Exercise 1

# Complete solution - Task 1 to Task 6
# Order of elements: track_name, unit_price, is_digital
track_list = [
    ("Beat it", 2.99, True),
    ("Billie Jean", 3.99, False),
    ("Thriller", 2.99, True),
    ("The Girl is Mine", 4.99, False)
]


def get_user_choice():
    print("Search options:")
    print("1. View all tracks")
    print("2. Search by track title")
    print("3. Search by price range")

    user_choice = int(input("Please enter your choice"))
    return user_choice


def display_all_tracks():
    if track_list:
        for title, price, is_digital in track_list:
            print(f"Title: {title}, Price: {price}, Available in digital form: {is_digital}")
        print(f"Found ({len(track_list)}) tracks in the media store")
    else:
        print("Sorry, no tracks available at the moment! Please check again later.")


def search_by_title():
    search_track_name = input("Enter the name of the track you want to search").lower()
    is_found = False
    for title, price, is_digital in track_list:  # better readability
        if search_track_name.lower() in title.lower():  # search name partially matches track title
            print(f"Title: {title}, Price: {price}, Available in digital form: {is_digital}")
            is_found = True

    if not is_found:
        print("Sorry, no tracks found matching your input.")


def search_by_price_range():
    min_price = float(input("Enter the minimum price: "))
    max_price = float(input("Enter the maximum price: "))

    if min_price > max_price:
        print("Minimum price cannot be larger than maximum price!")
        return

    for title, price, is_digital in track_list:
        if min_price <= price <= max_price:
            print(f"Title: {title}, Price: {price}, Available in digital form: {is_digital}")


user_choice = get_user_choice()
if user_choice == 1:
    # display all tracks
    display_all_tracks()

elif user_choice == 2:
    # display tracks that match the name
    search_by_title()

elif user_choice == 3:
    search_by_price_range()
else:
    print("Incorrect input. Please enter 1 or 2")


# Task 7

def get_user_choice():
    print("Search options:")
    print("1. View all tracks")
    print("2. Search by track title")
    print("3. Search by price range")
    print("4. Search by title and price range")


def search_tracks(search_title=None, min_price=0.0, max_price=float('inf')):
    found = False
    # if user enters search_title, search by title
    # if user enters price range, search by price range
    for title, price, is_digital in track_list:
        if search_title in title.lower() and min_price <= price <= max_price:
            print(f"Title: {title}, Price: {price}, Available in digital form: {is_digital}")
            found = True

    if not found:
        print("Sorry, no tracks found matching your input.")


if user_choice == 3:
    search_title = input("Enter the title to search: ")
    min_price = float(input("Enter the min. price to search: "))
    max_price = float(input("Enter the max. price to search: "))
    search_tracks(search_title, min_price, max_price)  # call with all parameters/positional arguments
    search_tracks(min_price=min_price, max_price=max_price,
                  search_title=search_title)  # call without order, keyword arguments
    search_tracks(search_title=search_title)  # call using optional parameter search_title

# Optional parameter passing - user can skip entering values
if user_choice == 3:
    search_title = input("Enter the title to search: ")
    input_min_price = input("Enter the min. price to search: ")
    if input_min_price:
        min_price = float(input_min_price)
    input_max_price = input("Enter the max. price to search: ")
    if input_max_price:
        max_price = float(input_max_price)
    search_tracks(search_title=search_title, min_price=min_price, max_price=max_price)

# Task 8
if user_choice == 1:
    # display all tracks
    display_all_tracks()
elif user_choice == 2:
    # display tracks that match the name
    search_track_name = input("Enter the name of the track you want to search").lower()
    search_tracks(search_title=search_track_name)
elif user_choice == 3:
    min_price = float(input("Enter the min. price to search: "))
    max_price = float(input("Enter the max. price to search: "))
    search_tracks(min_price=min_price, max_price=max_price)
elif user_choice == 4:
    search_title = input("Enter the title to search: ")
    min_price = float(input("Enter the min. price to search: "))
    max_price = float(input("Enter the max. price to search: "))
    search_tracks(search_title=search_title, min_price=min_price, max_price=max_price)
else:
    print("Incorrect input. Please enter 1 or 2")

# Exercise 2
# Complete solution

## DB
album_name, artist_name, genre_name = "Thriller", "Michael Jackson", "Pop"

track_list = [
    ("Beat it", 2.99, True),
    ("Billie Jean", 2.99, False),
    ("Thriller", 2.99, True),
    ("The Girl is Mine", 2.99, False)
]


### Functions are defined here
def get_user_choice():
    print("\nAdmin action options:")
    print("1. View all tracks")
    print("2. Add a new track")
    print("3. Update track price")
    print("4. Delete a track")
    print("5. Exit")

    user_choice = int(input("Please enter your choice"))
    return user_choice


def display_all_tracks():
    print("Showing all available tracks:")
    for title, price, is_digital in track_list:
        print(
            f"{track_list.index((title, price, is_digital)) + 1}. Title: {title}, Price: {price}, Available in digital format: {is_digital}")


def add_track():
    # add a new track
    title = input("Enter the track title")
    unit_price = float(input("Enter the unit price of the track"))
    digital_media = input("Is the track available in digital format (Y/N)?")
    is_digital = False
    if digital_media == "Y":
        is_digital = True

    new_track = (title, unit_price, is_digital)

    track_list.append(new_track)  # added at the end of the list
    print("The new track has been added to the media store. The updated track list is: ")
    print(track_list)  # can you reuse


def update_track():
    # find a track and then update
    search_title = input("Which track do you want to update? Enter the title: ")
    idx, track = find_track(track_title=search_title)
    new_price = float(input("Enter the updated unit price of the track"))
    edited_track = (track[0], new_price, track[2])

    if idx is None:
        print("Sorry, no track matching the title was found.")
    else:
        track_list[idx] = edited_track
        print("Successfully updated track details. Here's the updated list:")
        display_all_tracks()


def delete_track():
    # find a track and then delete
    search_title = input("Which track do you want to delete? Enter the title: ")
    idx, track = find_track(track_title=search_title)

    if idx is None:
        print("Sorry, no track matching the title was found.")
    else:
        track_list.remove(track)
        print("Successfully deleted track details. Here's the updated list:")
        display_all_tracks()


def find_track(track_title):
    for track in track_list:
        if track_title.lower() in track[0].lower():
            return track_list.index(track), track
    return None


## Input, Process, Output

is_continue = True

while is_continue:

    user_choice = get_user_choice()
    if user_choice == 5:
        is_continue = False
        print("Goodbye!")
    elif user_choice == 1:
        display_all_tracks()

    elif user_choice == 2:
        add_track()

    elif user_choice == 3:
        update_track()

    elif user_choice == 4:
        delete_track()
    else:
        print("Incorrect option. Please enter one of the options mentioned in the menu (1-4).")
