# Exercise 1
# User Story 1:
# As a customer, I would like to see the tracks in the media store, so that I can choose the track to buy.
# Output: Track Details
# DB: Available track and its details
# Input: None
# Process: None


# # task 1.
# track_name = "Beat it"
# album_name = "Thriller"
# artist_name = "Michael Jackson"
# track_genre = "Pop"
# unit_price = 0.99

# 1.
# print("Track name: " + track_name)
# print("Album name: " + album_name)
# print("Artist name:", artist_name)
# print("Track genre: " + track_genre)
# print("Unit price: " + unit_price)

# print("track name: %s" % track_name, "Album name: %s" % album_name, "Artist name: %s" % artist_name, "track genre: %s" % track_genre, "Unit price: %f" % unit_price)
# print("Track name: %s, Album name: %s, Artist name: %s, Track genre: %s, Unit price: %f" % (track_name, album_name, artist_name, track_genre, unit_price))
#
# print(f"Track name: {track_name}, Album name: {album_name}, Artist name: {artist_name}, Track genre: {track_genre}, Unit price: {unit_price}")

# # task 3.

# # 1.
# print(type(track_name))
# print(type(album_name))
# print(type(artist_name))
# print(type(track_genre))
# print(type(unit_price))


# # 3.
# track_name = "Beat it"
# album_name = "Thriller"
# artist_name = "Michael Jackson"
# track_genre = "Pop"
# unit_price = 1

# # task 3.
# print(type(track_name))
# print(type(album_name))
# print(type(artist_name))
# print(type(track_genre))
# print(type(unit_price))

#  4, 5 not made

# # 6.
# print(f"Track name: {track_name}, Album name: {album_name}, Artist name: {artist_name}, Track genre: {track_genre}, Unit price: {unit_price:.2f}")
































### Solutions

# # Exercise 1
# track_name = "Beat it"
# album_name = "Thriller"
# artist_name = "Michael Jackson"
# track_genre = "Pop"
# unit_price = 0.99
#
# ## use .2f to print two decimals
# print(f"Track name: {track_name}, Album name: {album_name}, Artist name: {artist_name}, Track genre: {track_genre}, Unit price: {unit_price:.2f}")
#
# # syntax and indentation solution
# track1 = "Beat it" #variable name starts with a number
# Album = "Thriller" #variable name starts with a capital
# album = "Dangerous" #variable name starts with a lowercase
# unit_price = 1.00 #variable name starts with a special character
# _genre = "Pop" #variable name starts with an underscore - allowed, but indicates a private variable in Object-oriented concepts
# is_global = True #variable name using a reserved keyword
# artist_name = "Michael Jackson" #variable name has a space or tab before/between the variable name
#
# # Exercise 2
# ## DB
# album_name = "Thriller"
# artist_name = "Michael Jackson"
# genre_name = "Pop"
#
# track_name1 = "Beat it"
# unit_price1 = 2.99
#
# track_name2 = "Billie Jean"
# unit_price2 = 2.99
#
# track_name3 = "Thriller"
# unit_price3 = 2.99
#
# track_name4 = "The Girl is Mine"
# unit_price4 = 2.99
#
# # Display available track details
# print(f"The album details are: ")
# print(f"Album Name: {album_name}, Artist: {artist_name}, Genre: {genre_name}")
#
# print(f"Tracks in this album are: ")
# print(f"Track 1: {track_name1}, Price: {unit_price1}")
# print(f"Track 2: {track_name2}, Price: {unit_price2}")
# print(f"Track 3: {track_name3}, Price: {unit_price3}")
# print(f"Track 4: {track_name4}, Price: {unit_price4}")
#
# ## Input
# num_tracks =int(input("How many tracks do you want to buy?"))
# print(num_tracks)
#
# ## Process
#
# # calculate total price of no. of tracks wished by the user
# total_price = num_tracks * unit_price1
# #print(type(num_tracks))
# #print(type(unit_price1))
# #print(total_price)
#
# # calculate the discounted price of an album
# album_price = unit_price1 * 4
# #print(album_price)
# discounted_album_price = album_price * 0.9
# #print(discounted_album_price)
#
# ## Output
# print(f"The total price of {num_tracks} tracks is: {total_price} EUR")
# print(f"Special Offer!!! If you buy the entire album, you get a discount of 10%!")
# print(f"Instead of {album_price} EUR, you pay only {round(discounted_album_price, 3):.2f} EUR!!")

