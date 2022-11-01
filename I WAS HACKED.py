name = 'Bubby'

message = f'{name} can we play today if you can'

print(message)

print('these are my best food \n '
      '1. Rice \n'
      '2. Bread and butter \n'
      '3. Pasta \n'
      '4. Plantain chips')

print('these are most of my feelings\n '
      '1. Funny \n'
      '2. Kind \n'
      '3.Playful \n'
      '4.Pro \n'
      '5.Calm \n'
      '6.Angry \n'
      '7.Strong \n'
      '8.Tryhard \n'
      '9.Sweaty \n'
      '10.Hungry')

print('these are the things I have in my house'
      '1.A laptop\n '
      '2.A xbox one \n'
      '3.A moniter \n'
      '4.A book \n'
      '5.A chair \n'
      '6.A gaming mouse \n'
      '7.A tv \n'
      '8.A garden \n'
      '9.Another tv \n'
      '10.A family picture')

numbers = 1, 22, 555, 557, 666, 66654, 3345, 45345345345, 4353454353444535

print(min(numbers))

print(max(numbers))

print(min(numbers))
nUmBeR = list(range(1, 777777))
print(nUmBeR)

friends = ['Fareed', 'Farrhan', 'Habib', 'Tobi', 'John', 'Jonathan',
           'Timi', 'Kenny', 'Mat']

sliced_list = friends[0:9]
print(sliced_list)

numbers = 1, 22, 555, 557, 666, 66654, 3345, 45345345345, 4353454353444535

print(len(numbers))
Counting = list(range(1, 100000))

print(3 * 10)

numb_list = list(range(3, 30))

print(numb_list)

print(2 ** 2 + 2 ** 3 + 2 ** 4 + 2 ** 5 + 2 ** 6 + 2 ** 7 + 2 ** 8 + 2 ** 9 + 2 ** 10)

print(numb_list)

OddNumber = 3, 7, 5, 9, 1, 13, 17, 15, 19, 11

JustNumber = 3, 7, 5, 9, 1, 13, 17, 15, 19, 11, 6, 8, 0, 2, 4, 10, 60, 80, 20, 0, 40, 100

take_out = list(range(1, 12))

print(take_out)

for OddNumbers in OddNumber:
    print(OddNumbers ** 3)

myProNumber = list(range(1, 100, ))

AmProClass = 'Farrhan', 'Fareed', 'Philip', 'Habib'

work = [print(number ** 3) for number in myProNumber]

print(AmProClass[0:2])

print('These are my pro people: ')
AmProBullSentance = [print(name) for name in AmProClass[0:3]]

# Assignment
# Create a list of 10 names,
# store the first 4 items of the list,
# store the 3 middle items of the list,
# And store the last 4 items of the list
# Loop over each of these lists using liszt comprehension
List = ['Farrhan', 'Roxy', 'Evox', 'Chicky', 'Boom Boom', 'Max', 'Levi', 'Meex', 'Makey', 'Toyiby']

Idrk = []
Idrk.append(List[0:3])
print(Idrk)
AmSheep = []
AmSheep.append(List[7:10])
print(AmSheep)
SheepBull = []
SheepBull.append(List[3:7])
print(SheepBull)

Food2 = ['Cabbeges', 'Grapes', 'Apple', 'Banana', 'Oranges', 'Mango', 'Limes', 'Lemon']
Food2P2W = [print(name) for name in Food2]
List = ['Farrhan', 'Roxy', 'Evox', 'Chicky', 'Boom Boom', 'Max', 'Levi', 'Meex', 'Makey', 'Toyiby']
print('This is some people that are cool:')
ChaChing = [print(name) for name in List]
Food1 = ['Ice-cream', 'Doughnuts', 'Bagels', 'Pizza', 'Chocolate', 'Bread']
Food1P2W = [print(name) for name in Food1]
# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
# (page 56). Make a copy of the list of pizzas, and call it friend_pizzas.
# Then, do the following:
# • Add a new pizza to the original list.
# • Add a different pizza to the list friend_pizzas.
# • Prove that you have two separate lists. Print the message My favorite
# pizzas are:, and then use a for loop to print the first list. Print the message
# My friend’s favorite pizzas are:, and then use a for loop to print the second
#list. Make sure each new pizza is stored in the appropriate list.
# 4-12. More Loops: All versions of foods.py in this section have avoided using
# for loops when printing to save space. Choose a version of foods.py, and
# write two for loops to print each list of foods.
# COMPREHENSION


meme = input('Enter first meme sentance:')
meme2 = input('Enter first meme2 sentance:')
if len(meme) > len(meme2):
    print(" meme is chunkier than meme2")
elif len(meme2) < len(meme):
    print("meme2 is chunkier than meme")
else:
    pass


answers = ['c', 'a', 'a', 'c', 'b', 'b', 'a', 'c or d', 'a', 'd', 'b', 'c',
           'c', 'd', 'c', 'a', 'a', 'c', 'd', 'b', 'a', 'a', 'd', 'a', 'b', 'c', 'a', 'b', 'd', 'c' ]

print(answers)

friend_pizzas = ['Pineapple Pizza', 'Cheese Pizza', 'Neapolitan Pizza', 'Chicago Pizza',
                 'New York-Style Pizza', 'Greek Pizza']
OGList = {'Cheese Pizza', 'Pepperoni Pizza', 'Veggie Pizza', 'Meat Pizza', 'Bacon Pizza',
          'Bqq Chicken Pizza'}
NewPizzaStatement = ['this is a new pizza named California Pizza is good as well as.']

for pizza in friend_pizzas:
    print(f'This{NewPizzaStatement}these amazing {friend_pizzas}')

print('My friend like these pizzas:')
theOgOglist = [print(name) for name in OGList]

print('I like these pizzas:')
TheOgOgFriend_pizza = [print(name) for name in friend_pizzas]