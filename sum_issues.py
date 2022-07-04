import pyttsx3
import wikipedia

engine = pyttsx3.init()

#Voice
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[1].id)   

def talk_function(text):
    engine.say(text)
    engine.runAndWait()

while True:

    user_input = input("User: ")
    user_input = user_input.lower()

    if user_input == "hello":
        talk_function("Hey, Hello");

    elif user_input == "how are you":
        talk_function("I am fine");
       
    elif user_input == "what is your name":
        talk_function("My name is GreenBot");

    elif user_input == "please do an addition":
       
        talk_function("Please provide me first number")
        num1 = int(input("Enter Number 1: "))
         
        talk_function("Please provide me second number")
        num2 = int(input("Enter Number 2: "))

        total = num1 + num2
        print(f'The total is: {total}')
        talk_function(f'The total value is: {total}')

    elif "who" in user_input:
        data = wikipedia.summary(user_input)
        print(data)
        talk_function(data)

    elif "what" in user_input:
        data = wikipedia.summary(user_input)
        print(data)
        talk_function(data)

    elif user_input == "please do an substraction":   

        talk_function("Please provide me first number")
        num1 = int(input("Enter Number 1: "))
         
        talk_function("Please provide me second number")
        num2 = int(input("Enter Number 2: "))

        total = num1 - num2
        print(f'The total is: {total}')
        talk_function(f'The total value is: {total}')

    elif user_input == "please do an multiplication":   

        talk_function("Please provide me first number")
        num1 = int(input("Enter Number 1: "))
         
        talk_function("Please provide me second number")
        num2 = int(input("Enter Number 2: "))

        total = num1 * num2
        print(f'The total is: {total}')
        talk_function(f'The total value is: {total}')

    elif user_input == "please do an division":   

        talk_function("Please provide me first number")
        num1 = int(input("Enter Number 1: "))
         
        talk_function("Please provide me second number")
        num2 = int(input("Enter Number 2: "))

        total = num1 / num2
        print(f'The total is: {total}')
        talk_function(f'The total value is: {total}')
        
        
    
    else:
        talk_function("I don't understand");