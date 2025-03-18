# Exercise 1

# Task 1
track_list = [
    ("Beat it", 2.99, True),
    ("Billie Jean", 2.99, False),
    ("Thriller", 2.99, True),
    ("The Girl is Mine", 2.99, False)
]

# Task 2
# display all tracks
if track_list:
    for track in track_list:
        print(f"Title: {track[0]}, Price: {track[1]}, Available in digital form: {track[2]}")
    print(f"Found ({len(track_list)}) tracks in the media shop")
else:
    print("Sorry, no tracks available at the moment! Please check again later.")

# Task 3
## Input, Process, Output

print("Search options:")
print("Enter 1 if you want to see all tracks")
print("Enter 2 if you want to search tracks by their title")

user_choice = int(input("Please enter your choice"))

if user_choice == 1:
    # display all tracks
    if track_list:
        for track in track_list:
            print(f"Title: {track[0]}, Price: {track[1]}, Available in digital form: {track[2]}")
    else:
        print("Sorry, no tracks available at the moment! Please check again later.")

elif user_choice == 2:
    # display tracks that match the name
    search_track_name = input("Enter the name of the track you want to search")
    is_found = False
    for track in track_list:
        if track[0] == search_track_name:
            print(f"Title: {track[0]}, Price: {track[1]}, Available in digital form: {track[2]}")
            is_found = True
            break
    if not is_found:
        print("Sorry, no tracks matching your request were found.")
else:
    print("Incorrect input. Please enter 1 or 2")

# Task 4
## Input, Process, Output

print("Search options:")
print("Enter 1 if you want to see all tracks")
print("Enter 2 if you want to search tracks by their title")

user_choice = int(input("Please enter your choice"))

if user_choice == 1:
    # display all tracks
    if track_list:
        for track in track_list:
            print(f"Title: {track[0]}, Price: {track[1]}, Available in digital form: {track[2]}")
        print(f"Found ({len(track_list)}) tracks in the media store")
    else:
        print("Sorry, no tracks available at the moment! Please check again later.")

elif user_choice == 2:
    # display tracks that match the name
    search_track_name = input("Enter the name of the track you want to search").lower()
    print(search_track_name)
    for track in track_list:
        # if track[0].lower() == search_track_name: # exact match
        if search_track_name.lower() in track[0].lower():  # search name partially matches track title
            print(f"Title: {track[0]}, Price: {track[1]}, Available in digital form: {track[2]}")
else:
    print("Incorrect input. Please enter 1 or 2")

## Exercise 2
# Complete solution for all tasks
## Input, Process, Output

is_continue = True

while is_continue:
    print("\nAdmin action options:")
    print("1. View all tracks")
    print("2. Add a new track")
    print("3. Update a track")
    print("4. Delete a track")
    print("5. Exit")

    user_choice = int(input("Please enter your choice"))

    if user_choice == 5:
        is_continue = False
        print("Goodbye!")
    elif user_choice == 1:
        print("Showing all available tracks:")
        for track in track_list:
            print(
                f"{track_list.index(track)}. Title: {track[0]}, Price: {track[1]}, Available in digital format: {track[2]}")

    elif user_choice == 2:
        # add a new track
        title = input("Enter the track title")
        unit_price = float(input("Enter the unit price of the track"))
        digital_media = input("Is the track available in digital format (Y/N)?")
        is_digital = False
        if digital_media == "Y":
            is_digital = True

        new_track = (title, unit_price, is_digital)
        print(new_track)

        # track_list.append(new_track) # added at the end of the list
        track_list.insert(0, new_track)  # insert at the beginning of the list
        print("The new track has been added to the media store. The updated track list is: ")
        print(track_list)

    elif user_choice == 3:
        # check the next exercise and add appropriate error/exception handling
        index = int(input("Which track do you want to update? Enter the index: "))
        title = input("Enter the updated track title")
        unit_price = float(input("Enter the updated unit price of the track"))
        digital_media = input("Is the track available in digital format (Y/N)?")
        is_digital = False
        if digital_media == "Y":
            is_digital = True
        edited_track = (title, unit_price, is_digital)
        track_list[index] = edited_track

    elif user_choice == 4:
        # delete a track by index
        # index = int(input("Enter the index of the track that you want to delete"))
        # if index < len(track_list):
        #    deleted_track = track_list.pop(index)
        #    print(f"{deleted_track} has been removed from the track list.")
        # else:
        #    print(f"Invalid index, please choose an index between 0 and {len(track_list)-1}")

        # find a track and then delete
        title = input("Enter the title of the track you want to delete")
        is_found = False
        for track in track_list:
            if title.lower() in track[0].lower():
                track_list.remove(track)
                print(f"{track} has been removed from the track list.")
                is_found = True
                break
        if not is_found:
            print("Sorry, no track matching the title was found.")
    else:
        print("Incorrect option. Please enter one of the options mentioned in the menu (1-4).")

# Exercise 3

# Task 1
print("\nAdmin action options:")
print("1. View all tracks")
print("2. Add a new track")
print("3. Update a track")
print("4. Delete a track")
print("5. Exit")

try:
    user_choice = int(input("Please enter your choice"))
except ValueError:
    print("Numeric input expected. Please enter a no. between 1 and 5.")

# Task 2
track_list = [
    ("Beat it", 2.99, True),
    ("Billie Jean", 2.99, False),
    ("Thriller", 2.99, True),
    ("The Girl is Mine", 2.99, False)
]

try:
    index = int(input("Enter the index of the track that you want to delete"))
    deleted_track = track_list.pop(index)
except ValueError:
    print("Numeric value expected. Please enter a number.")
except IndexError:
    print("You entered an index that does not exist. Please enter an index that is in range.")