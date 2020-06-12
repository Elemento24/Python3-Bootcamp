with open('data4.txt', 'w') as file:
    file.write('Here is the first statement!\n')
    file.write('Hey Guys, nice to meet you all!\n')
    file.write('Let us got & check it out!\n')

# When we want to write in a file, 'w' flag is used
# When we use 'w' flag, it creates the file, if the file doesn't exist
# And if the file exists, it clears the content of the file and writes ...
# ... the specified content in the file, that is, it overwrites the content of the file
