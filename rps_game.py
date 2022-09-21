

from multiprocessing import RLock


human_turn = input('input human turn: ')
computer_turn = input('input computer turn: ')

if human_turn == computer_turn:
    print('Draw!')

elif human_turn == 'rock' and computer_turn == 'scissors':
    print('Human Wins')
elif human_turn == 'paper' and computer_turn == 'rock':
    print('Human Wins')
elif human_turn == 'scissors' and computer_turn == 'paper':
    print('Human Wins')

else:
    print('Computer Wins!')
