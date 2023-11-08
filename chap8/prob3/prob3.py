print("Input your string . . .")


text_file = open("string.txt", "w")

while True:
    a = input(">> ")

    if a !="Q":
       text_file.writelines(a)
    
    else: 
        text_file.close()

        text_file = open("string.txt", "r")
        output = text_file.readlines()
       
        text_file.close()
        
        for line in output:
            print(line)
        
        break

        
