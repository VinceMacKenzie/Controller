import os
os.system('cls')
try:
    def print_menu():
        print("="*15)
        print("1: Script futtatása")
        print("2: Mapolás")
        print("3: Kilépés\n")
    print_menu()

    def choice_1():
        os.system('python Mute.py')


    choice = input("Menüpont: ")
    if choice != "1" and choice != "2" and choice != "3":
        print("hiba")
    if choice == "1":
        choice_1()
    elif choice == '2':
        print("majd megcsinálom")
    elif choice == "3":
        print("Kilépés")
        exit()
except:
    pass