# Who Wants to be a Millionare?
# By Marissa Salas for Programming Digital Media
# creation of classes game, player, question.

# version 1: list of titles, player selects author
# version 2: list of paragraph, player selects title and author

# test dataset dictionary - a collection which is unordered, changeable and does not allow duplicates.


#"Who wants to play, Who Wants to be a Millionare? "

#%%
import random
from books import books
import gutenberg



#%%
# This is the statement of the rules of the game

rules = "\nTo play you enter your name below. You start with $100. For each correct answer you double your money at each level. \nAfter reaching 15 levels you win, one Million dollars! \n***But one wrong answer ends the game and you leave with nothing.***" 


# A Class is "blueprint" (ie Car) for creating objects like a cookie cutter to make cookies (many objects)
# think of the __init__ assigns properties (ie color)and the functions inside are like the behaviors (ie speed)
# this gets the players name
class Player:
    def __init__(self, name):
        self.name = name
        print(f"{name} are you ready to play Who wants to be a Millionare?")

#this selects the questions randomly
class Question:
    def __init__(self, quiz, rand1, rand2, rand3):
        self.question = "Who is the author of the book: " + quiz["title"]
        self.author = quiz["author"]
        self.quiz = quiz

    def get_question(self):
        return self.question

    def get_author(self):
        return self.author
    
    def ask(self):
        return f"Who is the author of the book: {self.quiz['title']}"

        
class Game:
    # def __init__(self, rules, users_choice, correct_answer): handles the basics of the game
    def __init__(self):
        # self.rules = rules
        # self.users_choice = users_choice
        # self.correct_answer = correct_answer
        self.level = 1
        self.player = None
        self.prize = ["$100","$200","$300", "$500", "$1,000", "$2,000", "$4,000","$8,000","$16,000","$32,000", "$64,000", "$125,000", "$250,000", "$500,000", "$1 Million"]
        self.asked_questions = []

    def start(self):
        print(rules)
        players_name = input("Enter your name: ")
        self.player = Player(players_name)
        self.level = 1

    def end_game(self):
        print("The Game has ended.")
        print(f"You got to level {self.level} the {self.prize [self.level -1]} level.")

    def validate_user_answer(self, choice):
        if str.upper(choice) in ["A", "B", "C", "D"]:
            return True
        else:
            return False



    def process_answer(self, question, a, b, c, d):
        choices = {
            'A': a["author"],
            'B': b["author"],
            'C': c["author"],
            'D': d["author"]
        }
        
        user_answer = input("What's your final answer? (A, B, C, or D): ")
        valid_choice = self.validate_user_answer(user_answer)
        # print("The user input validity is : ", is_valid)

        while not valid_choice:
            print("That's an invalid choice. Please enter a A, B, C or D")
            user_answer = input("What's your final answer? (ABCD): ")
            valid_choice = self.validate_user_answer(user_answer)

        
        user_answer = str.upper(user_answer)
        user_answer = str.lower(choices[user_answer])
        correct_answer = question. get_author()
        correct_answer = str.lower(correct_answer)

        if(user_answer == correct_answer):
            self.level += 1
            print(f"Congratulations, you moved to next level {self.level}!")
            return True
        else:
            print("Sorry that was incorrect. \nThe correct answer was ", str.title(correct_answer))
            self.end_game()
            return False


        
    def process_question(self):     #select the correct question and answer and 3 random others
        print("Loading question...")
        a = gutenberg.fetch_random_book_data()
        b = gutenberg.fetch_random_book_data()
        c = gutenberg.fetch_random_book_data()
        d = gutenberg.fetch_random_book_data()
       
        questions_pool = [a, b, c, d]
        random_four_books = random.sample(questions_pool, 4)

        correct_book = random_four_books[0]     #in a list the first element is zero 
        random_book1 = random_four_books[1]
        random_book2 = random_four_books[2]
        random_book3 = random_four_books[3]

        question = Question(correct_book, random_book1, random_book2, random_book3)
        
        #self.asked_questions.append(correct_book)
        print(f"LEVEL: {self.level}\n#######################################")
        print(question.ask())
        #print(f"Who is the author of the book: {books[question.quizID]['title']}")
        print(f"Is it: \nA: {a['author']}\nB: {b['author']}\nC: {c['author']}\nD: {d['author']}")
        
        next_round = self.process_answer(question, a, b, c, d)
        if next_round:
            self.process_question()
        else:
            return

    def proceed_decision(self):
        decision = input("Do you want to play the game again? (Y/N) ")
        decision = str.lower(decision)
        valid_decision = decision == "y" or decision == "n"
        while not valid_decision:
            print("Invalid entry. Can only accept Y or N. Restarting.")
            decision = input("Do you want to play the game again? (Y/N) ")
            valid_decision = decision == "y" or decision == "n"
        if decision == "y":
            return True
        elif decision == "n":
            return False

    
if __name__ == "__main__":
    game = Game()
    game.start()
    proceed = True
    while proceed:
        game.start()
        game.process_question()
        proceed = game.proceed_decision()
    



# class Player:
#     def __init__(self, name):
#         self.name = name

#     def pick_answer(self):


    

# %%
