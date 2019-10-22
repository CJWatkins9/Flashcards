import random

terms = {
"55 KIAS":"Vx - (Best Angle of Climb)",
"67 KIAS": "Vy - (Best Rate of Climb)",
"111 KIAS": "Vno - (Normal Operating Speed)",
"149 KIAS": "Vne - (Never exceed speed)",
"98 KIAS": "Va - (Manuevering speed)",
"40 KIAS": "Vs - (Stall speed)",
"35 KIAS": "Vso - (Minimum flight speed in landing)",
"85 KIAS": "Vfe - (flaps extended)",
"60 KIAS": "Vg - (Glide speed)"
}

def main():
    menu = None
    while menu != 4:
        print("\nDigital Flashcards for Cessna 152!\n1 - List Terms\n2 - Guess Random Definition\n3 - View term-definition pairs\n4 - Exit")
        menu = input("\t\tEnter menu option: ")
        if menu == "1":
            print("\n")
            for term, definition in terms.items():
                print(term, definition)
            input("\n\tPress Enter to return to Main Menu. \n")
        elif menu == "2":
            print("\n\t\tType 'Exit' to return to main Menu \n")
            def generate_question():
                term, definition = random.choice(list(terms.items()))
                print("\n\t" + definition + "\n")
                return term
            term = generate_question()
            guess = None
            while guess != 'exit':
                guess = input("\tWhat is the speed? ").upper()
                if guess == term:
                    print('Correct!')
                    if input("\tAnother definition? (y/n)").lower() in ["y", "yes"]:
                        term = generate_question()
                    else:
                        break
                else:
                    print('\tThat is not correct.')
        elif menu == "3":
            print("\n\t\tType 'Exit' to return to main Menu \n")
            exit = None
            while exit != "exit":
                term, definition = random.choice(list(terms.items()))
                print(term + ":" + definition)
                exit = input("").lower()
        elif menu == "4":
            print("\nThanks you for using my flashcards!")
            quit()
        else:
            print('\nThat is not a valid option.')




if __name__ == "__main__":
    main()


            
