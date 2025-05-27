#Michael Stroup
#1/24/25
#Magic 8 Ball
#Init
import time
import random
#List of responses
magic8_list = ["yes", "No", "Most definitely", "Most definitely not", "Perchance", "Perchance not", "Why would you think otherwise?", "Why would you think that?", "Most Conceivably", "Most Inconceivably", "uncertain as of now", "It is certain", "We must discuss it with the fates.... no", "We must discuss it with the fates.... yes", "You don't really think that, do you?"]
#Fun
def game():
    #Welcome
    print("Welcome to the home of the Magic 8 Ball. Please ask only yes or no questions.")
    #Loop
    while True:
        try:
            print("You may ask your question, and it shall confer with fate...\n")
            #User question
            question = input("Ask your question here:")
            print(question)
            #Response
            print("Shake...")
            time.sleep(2)
            print("Shake...")
            time.sleep(2)
            print("Shake...")
            time.sleep(2)
            print(random.choices(magic8_list))
            #Ask to play again or quit
            print("\nWould you like to ask more questions, or leave to fulfill your destiny?\n(yes or no)")
            play_again = input("Enter yes or no")
            if play_again == "yes":
                print("Discussing destiny...\n")
            else:
                print("Fullfill your destiny and rate us five stars...")
                break
        except:
            print("Please only ask yes or no questions ending with a ?")

#Main
game()
