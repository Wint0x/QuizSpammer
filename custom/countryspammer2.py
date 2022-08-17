from time import perf_counter, sleep as s
from pyautogui import typewrite as spammer
import sys


START = perf_counter()
spammer.PAUSE = 0

def get_list():
    #Get file content in form of list, note that the file must contain strings separated by comma.
    with open('example.txt', 'r') as f:
        answers = f.read()
        answers = list(map(lambda x: x.replace("\n",""), answers.split(',')))
    return answers

#debug


print("You have 5 seconds to find find your quiz's entry box")
print(f"\nSending: {len(get_list())} words!\n")

answers = get_list()

s(5)

for word in answers:
    spammer(word,interval=0)

FINISH = perf_counter()

print(f"Finished in: {round(FINISH-START,2)} seconds!")
input()
