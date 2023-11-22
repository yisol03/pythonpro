print("Input your string...")

text_file = open("write_read.txt", "w")
while True:
    n = input(">>> ")
    if n == 'Q':
        break
    text_file.write(n)
    text_file.write("\n")
text_file.close()
print("Write process has been finished\n\n\n")

print("Your inputs are below..")
text_file = open("write_read.txt", "r")
whole_thing = text_file.read()
print(whole_thing)
text_file.close()
