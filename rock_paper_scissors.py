import random

def play():
    choices = ['rock', 'paper' , 'scissors'],
    user_choices = input("Enter rock, paper, or scissors: ")
    computer_choices = random.choice(choices[0])

    print (f"Computer choices: {computer_choices}")

    if user_choices ==computer_choices:
        return "It's a tie!"
    
    if is_win(user_choices, computer_choices):
        return "You win!"
    
    return "You Loose!"

    def is_win(player, opponent):
        if (player =='rock' and opponnennt =='scissors') or (player =='scissors' and opponent == 'paper') or (player =='paper' and opponent == 'rock'):
            return True
        return False
     
print(play())