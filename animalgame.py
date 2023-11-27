# %% [markdown]
# # 1_animal_game

# %%
from copy import copy

class AnimalNode:
    def __init__(self, question):
        self.question = question
        self.yes_child = None
        self.no_child = None

    # Return 'a' or 'an' as appropriate for this animal's name.
    def article(self):
        vowels = ('a', 'e', 'i', 'o','u')
        if self.question[0] in vowels:
            return 'an'
        else:
            return 'a'
    

    # Return the animal's name with an article.
    def full_name(self):
        if self.is_leaf():
            return self.article() + ' ' + self.question

    # Return True if this is a leaf node (which represents an animal).
    def is_leaf(self):
        if self.yes_child == None and self.no_child == None:
            return True

    # Ask this node's question and move to the appropriate child.
    # Return True if we keep playing.
    def ask_question(self):
        print("test 1")
        print(self.__dict__)

        if not self.is_leaf():
            answer=input(self.question).lower()
            print("test 2  " + answer)
            print(self.__dict__)
            if answer == 'q':
                return False
            elif answer == 'y':
                print("test 3")
                return self.yes_child.ask_question()
            elif answer == 'n':
                print("test 4")
                return self.no_child.ask_question()
        else:
            answer2 = input(f'Is {self.question} the right animal? ')
            
            if answer2 == 'q':
                return False
            elif answer2 == 'y':
                print("test 44")
                print("You have found the animal")
            elif answer2 == 'n':
                print("We did not find the animal")
                new_animal_str=input("Please input the animal? ")
                new_animal= AnimalNode(new_animal_str)
                question = input(f'Can you provide a question to distinquish between {self.full_name()} and {new_animal.full_name()}')
                
                first_animal = self
                self.question = question
                self.no_child = first_animal              
                self.yes_child = new_animal
                
                return True

# %%
def play_game():
    # Initialize the tree.
    root = AnimalNode('platypus')

    # Display instructions.
    print('Answer y for Yes, n for No, and q for Quit\n')

    # Repeat until the user quits.
    while root.ask_question():
        pass

# %%
# Play.
play_game()

# %%


