import random

# Setting Up

name = "Alex"
question = "Is this project worth it?"

answer = ""

# Generating a Random Number

random_number = random.randint(1, 9 + 4)
# print(random_number)

# Control Flow

if random_number == 1:
    answer = "Yes - definitely"
elif random_number == 2:
    answer = "It is decidedly so"
elif random_number == 3:
    answer = "Without a doubt"
elif random_number == 4:
    answer = "Reply hazy, try again"
elif random_number == 5:
    answer = "Ask again later"
elif random_number == 6:
    answer = "Better not tell you now"
elif random_number == 7:
    answer = "My sources say no"
elif random_number == 8:
    answer = "Outlook not so good"
elif random_number == 9:
    answer = "Very doubtful"
elif random_number == 9 + 1:
    answer = "Nap first, then yes"
elif random_number == 9 + 2:
    answer = "Ask me after coffee"
elif random_number == 9 + 3:
    answer = "Not in this economy"
elif random_number == 9 + 4:
    answer = "The voices told me so"
else:
    answer = "Error"

# Seeing the Result

# name = ""
if name == "":
    print("Question: " + question)
else:
    print(name + " asks: " + question)

# question = ""
if question == "":
    print("Be silent, close your eyes, and run...")
else:
    print("Magic 8-Ball's answer: " + answer)
