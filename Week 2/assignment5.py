# open the file in write mode
file = open("games.txt", "w")
 
# use a loop to get 3 video games from the user
for i in range(3):
    game = input("enter a favorite video game: ")
    # write each game to the file followed by a newline character
    file.write(game + "\n")

# close the file
file.close()
 