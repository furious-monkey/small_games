import random

print ("Mad Libs!")
print ("Enter an example of each. Remember to use quotation marks.")

random_name = input('Random name: ')
your_name = input('Your name: ')
place = input('Place: ')
adjective = input('Adjective, ex. weird: ')

adjs = ["Crazy", "Nice", "Lovely", "Gross"]
verbs = ["met", "proposed to", "robbed", "pushed"]
prepositions = ["above the", "near the", "around the", "behind", "beside"]

print ((random.choice(adjs)) + " " + random_name + " " + (random.choice(verbs))  + " " + your_name + " " + (random.choice(prepositions))+ " " + adjective + " " + place)
