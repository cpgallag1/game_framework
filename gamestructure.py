# Some format notes and framework for adventure games:
# 1. classes will be you're friends, they let you make for example players accoridng to a template. 
# then you can define actions on these templates like say "attack" or "defend"
# 2. Structure it thios way:
#  a) an external gamestate valiable holding mor eor less everything you need to know about the game
#  b) a while loop that will call until the gamestate is complete
#  c) a home function that will read the gamestate and decide what the next phase is.
# See the bottom of this file for the implementation of this structure.
# Advantage of it is we don't need to write the whole flow of the game from top to bottom.
# The GameState variable records progress.
# The home function reads that state and then calls the next action based on that. 



from typing import List  # I'm importing this for typing hints.
# Typing hints in python are non-binding (You can say somethings a string, it might still work with a number), 
# but very useful for clarifying your code.
# When you declare a variable they let you say what kind of object is it, a string, int, or custom class
# This is super handy when trying to keep track of the methods available.
# If you're using VS code (and you should) when you give a function argument
# like def my_func(my_var):, you can add a typing hint so vscode knows it's a string like so:
# def  my_func(my_var: str)
# Now when you hit my_var. VScode will autosuggest methods available to strings.
# It will also extrapolate that if if you have my_var: List[str] then my_var[0] must be a string.

# Debugging and autocomplete tools in VScode are a subject unto themselves I can run you through some time.
# It will save you wrting a lot of print statements for debugging purposes.


# You may not have made it to custom classes yet. 
# They are just like the built in types in that you can create an instance of them,
# then call methods and properties on them.
# Super useful for tracking structured data in one place like all of a players stats.
class Item():
    def __init__(self, name: str, attack_bonus: int) -> None:
        self.name = name
        self.attack_bonus = attack_bonus

    def __str__(self) -> str:
        return self.name

class Player():
    # Functions defined under a class definition are called methods, like the methods you'd call on a string.
    # You call them in the same way: variable_name.method_name(args)
    # "dunder" doubleunderscore methods used below. These usually explain how an operation implied by
    # standard syntax should be done.
    # e.g. The __add__() method in Python specifies what happens when you call + on two objects. 
    # When you call obj1 + obj2, you are essentially calling obj1.__add__(obj2).
    # If it's two integers it will add them together, if it's two strings it concatenates them.
    def __init__(self, name: str, hp: int, items: List[Item], attack: int = 5) -> None:  # Note the default assignment of 5 to attack
        # __init__ is the function implicitly called when we instantiate a new instance of a clas, e.g.:
        # charlie = Player("Charlie", 100, ["blunderbus"], 7)
        # self, refers to the instance itself and doesn't need an argument to stand in for it when the method is called
        # it's implicit in the fact it's being called as a method "variable.method_name()"
        self.name = name  # You'll see lines like this in __init__ all the time, 
        self.hp = hp  #     We are setting the valiable passes after the class name on instatiation
        self.items = items  # to a property we can access via dot notation:
        # charlie = Player("Charlie", 100, ["blunderbus"], 7)
        # charlier.hp => returns 100

    def __str__(self) -> str:
        # The __str__ method determines what will appear when you call print on your instance.
        return f"Name: {self.name}, HP:{self.hp}"
        # print(charlie) =>  Name: Charlie, HP:100
        # This f"Literal Text{variable}" syntax is by far the best way to interpolate strings etc. 

class HumanPlayer(Player): # When defining a class the variable in the brackets after it is not an argument
    # It is a super class, it says this new class should take on all the properties and methods of this old one,
    # barring anything overwritten or changed below.
    def __init__(self, name: str, hp: int, items: List[Item], teammates: List[Player]) -> None:
        self.teammates = teammates
        super().__init__(name, hp, items)  # super(). refers to the super class in this case Player.
        # So here we do something new, assign teammates, which would overwrite the __init__ method and 
        # leave name, hp, and items unassigned as properties of the HumanPlayer instance,
        # so we after assigning teammates we access the Player class it's based on with super(). and run it's init
        # logic on our own instance with super.__init__(name, hp, items)  

class GameState():
    def __init__(self) -> None:
        self.level = 0  # We'll use this to keep track of where in the game users are.
        self.complete = False  # Exit condition for our while loop.

game_state = GameState()

def level_0():
    # Charachter creation here:
    # name = input(), etc...
    # game_state.human_player = HumanPlayer(name...)
    # Increment the round on completion, or don't if they lose, in which case it will start again.:
    # if victory:
    #     game_state.level = 1
    pass # placeholder do nothing command as a empty function is invalid syntax

def level_1():
    # do next level shit
    # game_state.level = 2
    pass
    
    
def home():
    levels = {
        0: level_0,
        1: level_1,
    }
    level = levels[game_state.level]
    level()

while not game_state.complete:
    home()