print("Input your string . . .")


text_file = open("string.txt", "w")

while True:
    a = input(">> ")

    if a !="Q":
       text_file.write(a+"\n")
    
    else: 
        text_file = open("string.txt", "r")
        output = text_file.readline()
        print(output,("\n"))

        break

        
