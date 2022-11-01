key = 69
name = 'Fon'
score = 0

username = input('Enter your super smug username here:')
password = int(input('Enter your super smug password here:'))
if username == name and password == key:
    print('YoU cAn NoW tAkE tHe SmUg TeSt >:) ')
elif username == name and password != key:
    print('Username is correct but sadly key is incorrect')
elif username != name and password == key:
    print('Username is incorrect but fortunatley the  key is correct')
else:
    print('Your deatails are incorrect')
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
            answer = ' Giant Antarctic Blue Whale'
            if question3 == answer:
                print('Correct Answer')
                score += 10
                print(f'You have {score} points ')
FinalScore = 30
print(f'This is the end of the quiz/exam \n {username.title()} '
      f'you have a total of {FinalScore} you got a A+ well done')
