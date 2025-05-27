#Michael Stroup
#Slot Machine
#1/28/25
#Init
import time
import random
credit = 10
#4 hearts, 4 diamonds, 3 spades, 3 clubs, 2 stars, 1 seven
slotList = [ "♥","♥","♥","♥", "♦","♦","♦","♦", "♠","♠","♠", "♣","♣","♣", "☆","☆", "7"]
#Fun
def game():
    global credit
    global slotList
    #Welcome
    print("Welcome to the Slot Machine! Select spin(1) to start.")
    while True:
        try:
            print("1. Spin \n2. Quit\n3. View Credit\n")
            action = int(input("Type 1-3"))
            #Playing the slot machine
            if action == 2:
                print("Play again soon.")
                break
            #Veiw remaining credit
            elif action == 3:
                print("Your Credit is: " + str(credit) + "\n")
            #Spin and credit removal
            elif action == 1:
                #How much bet
                print("How much credit would you like to bet?")
                while True:
                    print("Your credit is: " + str(credit))
                    bet = int(input("Enter a number"))
                    if bet > credit:
                        print("You can't bet that much. Try again")
                    else:
                        break
                credit = credit - bet
                print("You bet : " + str(bet))
                print("Spinning!")
                slot1 = random.choice(slotList)
                time.sleep(2)
                print(slot1)
                slot2 = random.choice(slotList)
                time.sleep(2)
                print(slot1 + slot2)
                slot3 = random.choice(slotList)
                time.sleep(2)
                print(slot1 + slot2 + slot3)
                #Outcome
                if slot1 == "7" and slot2 == "7" and slot3 == "7":
                    print("JACKPOT!!!!\n")
                    bet = bet * 100
                    credit = credit + bet
                    print("Your credit is: " + str(credit) + "\n")
                elif slot1 == slot2 and slot1 == slot3:
                    print("You Win!\n")
                    bet = bet * 20
                    credit = credit + bet
                    print("Your credit is: " + str(credit) + "\n")
                elif slot1 == slot2 or slot1 == slot3 or slot2 == slot3:
                    print("Two of a kind!\n")
                    bet = bet * 2
                    credit = credit + bet
                    print("Your credit is: " + str(credit) + "\n")
                else:
                    print("You lost:(\nBetter luck next time.\n")
                    print("Your credit is: " + str(credit) + "\n")
            print("Would you like to play again?")
            print("1. Play Again\n2. Quit")
            playAgain = int(input("Enter 1-2"))
            if playAgain == 1 and credit <= 0:
                print("Oh no! Looks like your out of credit.\nCome back with some more to play again.")
                break
            elif playAgain == 1:
                print("Reseting Slots!\n")
            else:
                print("Thanks for playing.")
                break
        #Error message
        except:
            print("Invalid input. Please type only a number")

#Main
game()
