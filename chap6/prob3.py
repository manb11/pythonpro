# 빈 딕셔너리를 생성
geek_dict = {"404":"clueless.", "Uninstalled":"being fired."}


# 메뉴 출력 함수
def print_menu():
    print("")
    print("0. Quit")
    print("1. Look up a Geek Term")
    print("2. Add a Geek Term")
    print("3. Redefine a Geek Term")
    print("4. Delete a Geek Term")
    print("")

# 루프를 사용하여 사용자와 상호작용
while True:
    print_menu()
    choice = input("choice: ")
    
    if choice == "0":
        print("Quit")
        break
    elif choice == "1":
        term = input("What term do you want me to translate?: ")
        if term in geek_dict:
            definition = geek_dict[term]
            print(f"{term}: {definition}")
        else:
            print(f"{term}not found.")
    
    elif choice == "2":
        term = input("New term: ")
        definition = input(f"{term} term meaning: ")
        geek_dict[term] = definition
        print(f"{term} Add successfull.")
    
    elif choice == "3":
        term = input("Redefine a Geek Term: ")
        if term in geek_dict:
            new_definition = input(f"term: ")
            geek_dict[term] = new_definition
            print(f"{term}successfully update.")
        else:
            print(f"{term}not found.")
    
    elif choice == "4":
        term = input("Delete term: ")
        if term in geek_dict:
            del geek_dict[term]
            print(f"{term} it was delete.")
        else:
            print(f"{term}not found.")
    
    else:
        print("It doesn't exist. try again.")

