print("Creating a text file with the write() method.")

text_file = open("write_it.txt", "w")
print("Reading the newliy created file.")
text_file.write("Line 1\n")
text_file.write("This is line 2\n")
text_file.write("That makes this line 3\n")
text_file.close()


print("\nCreating a text file with the writelines() method.")

text_file = open("write_it.txt", "w")
print("Reading the newly created file.")
lines = [ "Line 1\n", "This is line 2\n", "That makes this 3\n" ]
text_file.writelines(lines)
text_file.close()
