import json
import os
from sys import platform

def cl():
    if platform == 'win32':
        return os.system('cls')
    else:
        return os.system('clear')

cl()

todo = []

try: 
    with open('mylist.txt', 'r') as f:
        todo = json.load(f)

except:
    open('mylist.txt','w').close()

print("Welcome to your To-do List!!\n")

if not todo==[]:
    print("Today we are doing:\n") 
    for i,task in enumerate(todo):
        print(f"{i+1}. {task}")

print("\nOnce you have finished adding to your list, type 'finish'\nTo clear your list, just type 'clear'.\n")

while True:
    a = input("What are you doing today? ")
    if a.lower() == "finish":
        break
    elif a.lower() == "clear":
        open('mylist.txt','w').close()
        todo = []
        cl()
        print("List cleared.")
    elif a.lower() == "exit":
        print("Thanks for choosing JOSHY'S LISTS")
        exit() 
    else:
        todo += [a]

def betterclear(message):
    def clearscreen(func):
        def wrap():
            cl()
            print(f"---------  {message}  ---------\n")
            func()
            print(f"\n---------  {message}  ---------")
        return wrap
    return clearscreen

@betterclear("JOSHY'S LIST")
def showlist():
    while("" in todo):
        todo.remove("")
  
    if not todo == []:
        print("Today we will be doing:\n") 
        for i,task in enumerate(todo,1):
           print(f"{i}. {task}")
    else:
        print("There's nothing in your list!")

showlist()

with open('mylist.txt', 'w') as f:
    json.dump(todo, f)


input()


    


