import random
#CSC 221Magic 8 Ball Project by Anna Pfaff and Bianna Quiroga
# Class definition for Magic 8-Ball
class Magic8Ball:
    def __init__(self):
        # List of possible responses
        self.responses = [
            "It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely",
            "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes",
            "Signs point to yes", "Reply hazy, try again", "Ask again later",
            "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
            "Don’t count on it", "My reply is no", "My sources say no",
            "Outlook is not so good", "Very doubtful"
        ]

    # Method to get a random response
    def get_response(self):
        return random.choice(self.responses)

    # Method to handle user interaction
    def ask_question(self):
        while True:
            user_input = input("Do you have a question for the Magic 8-Ball? (yes/no): ").strip().lower()
            if user_input == 'no':
                print("Go elsewhere")
                break
            elif user_input == 'yes':
                question_type = input("Is it a yes or no question? (yes/no): ").strip().lower()
                if question_type == 'no':
                    print("Please ask a yes or no question to use the Magic 8-Ball.")
                else:
                    input("Once you have your question in mind, type 'Ask' to get a response: ")
                    print("Magic 8-Ball says:", self.get_response())
            else:
                print("Invalid input. Please answer with 'yes' or 'no'.")

            replay = input("Would you like to ask another question? (yes/no): ").strip().lower()
            if replay != 'yes':
                print("Thank you for playing the Magic 8-Ball game!")
                break

# Create an instance of the Magic8Ball class and start interaction
magic_ball = Magic8Ball()
magic_ball.ask_question()
