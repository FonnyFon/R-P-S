key = 21
name = 'Fon'


username = input('Enter your username here:')
password = int(input('Enter your password here:'))

if username == name and password == key:
    print('You can now take the car preview now \n ')



if username == name and password == key:
    print(f'Login Successful, \n Welcome {username}, You can take your car preview now')

    preview1 = input('This car is well know for its good looks and its amazing drifts. Would you like to buy?')
    answer = 'Maybe'
    if preview1 == answer:
        print('We will show this car after the preview')




        preview2 = input('This car is well known for famous people using it. Would you like to buy it?')
        answer = 'Yes'
        if preview2 == answer:
            print('The price for this car is 400 pounds')


            question3 = input('For the last thing we will ask you will you rate us out of 1/5?')
            answer = '5/5'
            if question3 == answer:
                print('Thanks I hope you enjoyed this preview. Bye Bye!')


    else:
        print('Incorrect Answer')


elif username == name and password != key:
    print('Username is correct and password is incorrect')
else:
    print('Login details are incorrect')


print(f'This is the end of the preview \n {username.title()} '
      f'you have bought 1 car well done')





