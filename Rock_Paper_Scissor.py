import random
options = ['rock','paper', 'scissor' ]
user_wins = 0
computer_wins = 0
print("Welcome to Rock-Paper-Scissor! ")
while True:
    user_input = input('Enter Rock/Paper/Scissor or Q to quit: ').lower()
    if user_input == 'q':
        break
    if user_input not in options :
        continue
    random_number = random.randrange(3)
    #'rock':0 ,'paper':1 , 'scissor':2 
    computer_guess = options[random_number]
    print('Computer guess', computer_guess )
    if user_input == 'rock' and computer_guess == 'scissor':
        print('You got LUCKY!')
        user_wins += 1
    elif user_input == 'paper' and computer_guess == 'rock':
        print('You got LUCKY!')
        user_wins += 1
    elif user_input == 'scissor' and computer_guess == 'paper':
        print('You got LUCKY!')
        user_wins += 1
    elif user_input == computer_guess :
        print('Draw')
    else:
        print('You lost :(')
        computer_wins += 1
print('You won', user_wins , 'times\n','Computer won', computer_wins , 'times\n') 
print('Goodbye! ')