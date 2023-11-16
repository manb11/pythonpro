print("Opening and closing the file.\n")

text_file = open("read_it.txt", "r")

print("Reading characters from the file.")
print(text_file.read(1))
print(text_file.read(5))
print("")

text_file.close()

text_file = open("read_it.txt", "r")

print("Reading the entire file at once.")
whole_thing = text_file.read()
print(whole_thing)
print("")

text_file.close()
 
print("Reading characters from a line.")
text_file = open("read_it.txt", "r")
print(text_file.readline(1))
print(text_file.readline(5))
print("")

text_file.close()

print("Reading one line at a time.")
text_file = open("read_it.txt", "r")
print(text_file.readline())

print(text_file.readline())

print(text_file.readline())
print("")

text_file.close()


print("Reading the entire file into a list.")
text_file = open("read_it.txt", "r")
lines = text_file.readlines()
print(lines)
print("")


text_file.close()

text_file = open("read_it.txt", "r")

a = input()

if a == 1:
    print("Line 1")
elif a == 2:
    print("This is line 2")
elif a == 3:
    print("This makes this line 3")
   
text_file.close()


print("Looping through the file, line by line.")
text_file = open("read_it.txt", "r")
for line in text_file:
    print(line)
print("")

text_file.close()
