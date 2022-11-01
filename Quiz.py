key = 21
name = 'Fon'
score = 0

username = input('Enter your username here:')
password = int(input('Enter your password here:'))

if username == name and password == key:
    print('You can now take the exam now \n ')



if username == name and password == key:
    print(f'Login Successful, \n Welcome {username}, You can take your good exam now')

    question1 = input('What is one of the well know W W E ?: ')
    answer = 'The Rock'
    if question1 == answer:
        print('Correct Answer')
        score += 10
        print(f'You have {score} points ')



        question2 = input('What is the best meme in the world?:')
        answer = 'Rick Roll'
        if question2 == answer:
            print('Correct Answer')
            score += 10
            print(f'You have {score} points ')

            question3 = input('What is largest thing in the world that is still alive? ')
            answer = 'Whale'
            if question3 == answer:
                print('Correct Answer')
                score += 10
                print(f'You have {score} points ')

    else:
        print('Incorrect Answer')


elif username == name and password != key:
    print('Username is correct and password is incorrect')
else:
    print('Login details are incorrect')

FinalScore = 30
print(f'This is the end of the quiz/exam \n {username.title()} '
      f'you have a total of {FinalScore} you got a A+ well done')





