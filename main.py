import random

CHOICES = ['r', 'p', 's']
opt = {
    'R': "Rock",
    'S': "Scissors",
    'P': "Paper"
}
def get_player_choice():
    
    player_choice = None
    while player_choice is None:
        player_choice = input('Please pick your Choice using only the first alphabets: \n(R)ock \n(P)aper \n(S)cissors \n\nPick: ')
        if player_choice.lower() not in CHOICES:
            print('Error!!!, please try again')
            player_choice = None
    return player_choice.lower()
def get_computer_choice():
    """computer randomly picks one of the valid choice"""
    computer_choice = random.randint(0, 2)
    computer_choice = CHOICES[computer_choice]
    return computer_choice
def is_draw(player_choice, computer_choice):
    """Check if game was a draw"""
    if player_choice == computer_choice:
        return True
def print_winner(player_choice, computer_choice):
    """Check winner"""
    if player_choice == 'r' and computer_choice == 's':
        print('Player wins!')
    elif player_choice == 's' and computer_choice == 'p':
        print('Player wins!')
    elif player_choice == 'p' and computer_choice == 'r':
        print('Player wins!')
    else:
        print('Computer wins!')
        print('%s beats %s' % (computer_choice, player_choice))
def play_game():
    """start game"""
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    if is_draw(player_choice, computer_choice):
        print("It's a tie, both players picked %s: " % player_choice)
    else:
        print("CPU: %s" % computer_choice)
        print("Player: %s" % player_choice)
        print_winner(player_choice, computer_choice)
if __name__ == "__main__":
    play_game()