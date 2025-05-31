# defining class called Album
class Album:
    #initialise the following elements
    def __init__ (self, album_name, album_artist, number_of_songs):
        self.album_name = album_name # to store album name
        self.album_artist = album_artist # to store album artist
        self.number_of_songs = number_of_songs # to store the number of songs within album

    def __str__(self):
        return f'({self.album_name}, {self.album_artist}, {self.number_of_songs})'

# creating a new list called album1, with 5 objects to it

# creating the strong
albums1 = []

# adding 5 album objects
album1 = Album("Alabaster Box", "Cece Winans", "12")
album2 = Album("The Sound", "Mary Mary", "10")
album3 = Album("Here I Am", "Marvin Sapp", "12")
album4 = Album("Believe", "Yolanda Adams", "11")
album5 = Album("Hero", "Kirk Franklin", "14")

# append the objects to the albums1
albums1.append(album1)
albums1.append(album2)
albums1.append(album3)
albums1.append(album4)
albums1.append(album5)

# print the album list
print("The albums listed in Album1: \n")
for album in albums1:
    print(album)

# Sort the list according to number of songs and print it out
# using the lambda sort method
# sorting from least to most number of songs per album

albums1.sort(key=lambda albums: albums.number_of_songs)

# print the number of songs
print("\nListed in order of number of songs: \n")
for album in albums1:
    print(album)

# swapping the element at index 0 of album1
# with the element at index 1

albums1[0], albums1[1] = albums1[1], albums1[0]

# print the result
print("\nAlbums list after swapping Album 1 and Album 2: \n")
for album in albums1:
    print(album)

# creating a new list called albums2

albums2 = []

# adding 5 album objects
album1 = Album("More Than This", "Cece Winans", "13")
album2 = Album("Look up Child", "Lauren Daigle", "9")
album3 = Album("I can only Imagine", "Mercy Me", "12")
album4 = Album("I speak Jesus", "Charity Gayle", "7")
album5 = Album("House of the Lord", "Phil Wickham", "5")

# append the objects to the albums1
albums2.append(album1)
albums2.append(album2)
albums2.append(album3)
albums2.append(album4)
albums2.append(album5)

# print the album2 list
print("\nThe albums listed in Album2: \n")
for album in albums2:
    print(album)

# Copying the albums from Album1 to Album2
albums2.extend(albums1)

print("\nThe album list of Album1 copied to Album2: \n")
for album in albums2:
    print(album)

# adding two more albums to albums2
album6 = Album("Dark side of the moon", "Pink Flyod", "9")
album7 = Album("Oops.... I Did it Again", "Brittany Spears", "16")

albums2.append(album6)
albums2.append(album7)

print("\nThe albums listed in Album2 including the new additions: \n")
for album in albums2:
    print(album)

# Sort Album2 alphabetically according to album name 
albums2.sort(key=lambda albums: albums.album_name)

# print Album2 in alphabetical order
print("\nAlbum2 in alphabetical order according to the Album Name: \n")
for album in albums2:
    print(album)

# search for particular album in Album2 and print out the index of the album
for i, album in enumerate(albums2):
  if album.album_name == 'Dark side of the moon':
    print(f'\nIndex of Dark Side of the Moon in Albums2 is: {i}')