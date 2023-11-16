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

text_file.close()

text_file = open("read_it.txt", "r")

a = int(input())  # Convert input to integer

for _ in range(a):
    line = text_file.readline()
    if not line:
        break
    print(line.strip(),"\n")

text_file.close()

print("\nLooping through the file, line by line.")
text_file = open("read_it.txt", "r")
for line in text_file:
   print(line.strip(),"\n")

text_file.close()



b = input("\n\nPress the enter key to exit.")

if b == "":
    print("")

