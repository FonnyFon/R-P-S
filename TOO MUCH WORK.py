import random
active = True
while active:
    score = 0
    options = ['Rok', 'Paper', 'Scissors']
    computer_choice = random.choice(options)
    user_choice = input("Enter your choice here!:").title()
    if user_choice == 'Rok' and computer_choice == 'Rok':
        print('It is a tie')
        print(f'Computer chooses {computer_choice}')
    elif user_choice == 'Rok' and computer_choice == 'Paper':
        print(f'Computer chooses {computer_choice}')
        print('You lose')
        score -= 1
        print(score)
    elif user_choice == 'Rok' and computer_choice == 'Scissors':
        print('You win')
        score += 1
        print(score)
        print(f'Computer chooses {computer_choice}')
    elif user_choice == 'Paper' and computer_choice == 'Paper':
        print('It is tie')
        print(f'Computer chooses {computer_choice}')
    elif user_choice == 'Paper' and computer_choice == 'Scissors':
        print('You lose')
        score -= 1
        print(score)
        print(f'Computer chooses {computer_choice}')
    elif user_choice == 'Paper' and computer_choice == 'Rok':
        print('You win')
        score += 1
        print(score)
        print(f'Computer chooses {computer_choice}')
    elif user_choice == 'Scissors' and computer_choice == 'Paper':
        print('You win')
        score += 1
        print(score)
        print(f'Computer chooses {computer_choice}')
    elif user_choice == 'Scissors' and computer_choice == 'Scissors':
        print('It is a tie')
        print(f'Computer chooses {computer_choice}')
    elif user_choice == 'Scissors' and computer_choice == 'Rok':
        print('You lose')
        score -= 1
        print(score)
        print(f'Computer chooses {computer_choice}')
