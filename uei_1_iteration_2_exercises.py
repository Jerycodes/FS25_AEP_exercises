# Exercise 1
# Task 1
album_name = "Thriller"
artist_name = "Michael Jackson"
genre_name = "Pop"

track_name1 = "Beat it"
unit_price1 = 2.99
is_digital1 = True

track_name2 = "Billie Jean"
unit_price2 = 2.99
is_digital2 = False


track_name3 = "Thriller"
unit_price3 = 2.99
is_digital3 = True

track_name4 = "The Girl is Mine"
unit_price4 = 2.99
is_digital4 = False

# Task 2
## Output
print("Thank you for your interest! We have the following tracks in digital form:")
print(f"Album name: {album_name}\t\t Artist: {artist_name}\t Genre: {genre_name}")
# if block is_digital1 start
if is_digital1:
    print(f"Track 1. Title: {track_name1}\t\t Price: {unit_price1}")
# if block end
# if block is_digital2 start
if is_digital2:
    print(f"Track 2. Title: {track_name2}\t\t Price: {unit_price2}")
# if block is_digital2 end
# if block is_digital3 start
if is_digital3:
    print(f"Track 3. Title: {track_name3}\t Price: {unit_price3}")
# if block end
# if block is_digital4 start
if is_digital4:
    print(f"Track 4. Title: {track_name4}\t\t Price: {unit_price4}")
# if block end

# Task 3
## Output

if is_digital1 or is_digital2 or is_digital3 or is_digital4:
    print("Thank you for your interest! We have the following tracks in digital form:")
    print(f"Album name: {album_name}\t\t Artist: {artist_name}\t Genre: {genre_name}")
    # if block is_digital1 start
    if is_digital1:
        print(f"Track 1. Title: {track_name1}\t\t Price: {unit_price1}")
    # if block end
    # if block is_digital2 start
    if is_digital2:
        print(f"Track 2. Title: {track_name2}\t\t Price: {unit_price2}")
    # if block is_digital2 end
    if is_digital3:
        print(f"Track 3. Title: {track_name3}\t Price: {unit_price3}")
    if is_digital4:
        print(f"Track 4. Title: {track_name4}\t\t Price: {unit_price4}")
else:
    print("Sorry, we do not have any tracks in digital form at the moment. Please come and check later.")

# Task 4
# DB
album_name, artist_name, genre_name, is_in_stock = "Thriller", "Michael Jackson", "Pop", True

track_name1, unit_price1, is_digital1 = "Beat it", 2.99, False
track_name2, unit_price2, is_digital2 = "Billie Jean", 2.99, False
track_name3, unit_price3, is_digital3 = "Thriller", 2.99, False
track_name4, unit_price4, is_digital4 = "The Girl is Mine", 2.99, False

# Output
if is_in_stock:
    if is_digital1 or is_digital2 or is_digital3 or is_digital4:
        print("Thank you for your interest! We have the following tracks in digital form:")
        print(f"Album name: {album_name}\t\t Artist: {artist_name}\t Genre: {genre_name}")
        # if block is_digital1 start
        if is_digital1:
            print(f"Track 1. Title: {track_name1}\t\t Price: {unit_price1}")
        # if block end
        # if block is_digital2 start
        if is_digital2:
            print(f"Track 2. Title: {track_name2}\t\t Price: {unit_price2}")
        # if block is_digital2 end
        if is_digital3:
            print(f"Track 3. Title: {track_name3}\t Price: {unit_price3}")
        if is_digital4:
            print(f"Track 4. Title: {track_name4}\t\t Price: {unit_price4}")
    else:
        print("Sorry, we do not have any tracks in digital form at the moment. Please come and check later.")
else:
    print("Sorry, this album is out of stock. Please check again later.")


# Exercise 2
# Task 1
# DB
album_name, artist_name, genre_name, is_in_stock = "Thriller", "Michael Jackson", "Pop", False

track_name1, unit_price1, is_digital1 = "Beat it", 2.99, True
track_name2, unit_price2, is_digital2 = "Billie Jean", 2.99, False
track_name3, unit_price3, is_digital3 = "Thriller", 2.99, True
track_name4, unit_price4, is_digital4 = "The Girl is Mine", 2.99, False

# Task 2
## Input
print("Limited Time Offer! Purchase the full album and enjoy a 10% discount!")
user_choice = input("Would you like to buy the full album (Y/N)?")
print(user_choice)

# Task 3
## Process
if user_choice == "Y":
    # apply discount
    album_price = unit_price1 + unit_price2 + unit_price3 + unit_price4
    discounted_price = 0.9 * album_price
else:
    num_tracks = int(input("How many tracks do you want to buy?"))
    # calculate total price
    total_price = unit_price1*num_tracks
    print(total_price)

# Task 4
## Output
if user_choice == "Y":
    print(f"Great! The album price including the discount is: {album_price} CHF.")
else:
    print(f"Thank you. The total price for {num_tracks} tracks is: {total_price} CHF.")


# Exercise 3
# Task 1
# DB
# Order of elements: album_name, artist_name, genre_name, is_in_stock
album1 = "Thriller", "Michael Jackson", "Pop", True

# Order of elements: track_name1, unit_price1, is_digital1
track1 = "Beat it", 2.99, True
track2 = "Billie Jean", 2.99, False
track3 = "Thriller", 2.99, True
track4 = "The Girl is Mine", 2.99, False