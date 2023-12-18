import random

name = input('What is your name? ')

question = input('Alright ' + name + ' What is your question? ')

answer = ''

random_number = random.randint(1, 12)

if random_number == 1:
    answer = 'Yes - definitely'
elif random_number == 2:
    answer = 'It is decidedly so'
elif random_number == 3:
    answer = 'Sure why not'
elif random_number == 4:
    answer = 'yeses all around'
elif random_number == 5:
    answer = 'My sources say absolutely'
elif random_number == 6:
    answer = 'Do not know many other ways to say yes...so yes'
elif random_number == 7:
    answer = 'My sources say no'
elif random_number == 8:
    answer = 'Outlook not so good'
elif random_number == 9:
    answer = 'Very doubtful'
elif random_number == 10:
    answer = "I'm not too sure"
elif random_number == 11:
    answer = 'Try again'
elif random_number == 12:
    answer = 'How about no'
else:
    answer = 'Error'

if name == '':
    print('Question: ' + question)
else:
    print(name + ' asks: ' + question + '?')

if question == '':
    print('No question asked')
else:
    print('Magic 8-Balls answer: ' + answer)

while True:
  try:
    survey = float(input('please rate how you enjoyed the Magic 8 Ball from 0-5: '))
    if survey < 0:
      print('Come on I am Trying my best it is random after all')
    elif survey <= 2:
      print('Sorry you are not satisfied with my service. I hope to make it better for you.')
    elif survey <= 5:
      print('Thanks for using Magic 8 Ball and we appreciate your rating')

    elif survey > 5:
      print('I am really glad you are enjoying my services and thank you for going above and beyond in your rating')
    break
  except ValueError:
    print('Invalid input. Please enter a valid number.')
