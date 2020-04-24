import json
import os
from sys import platform

def cl():
    if platform == 'win32':
        return os.system('cls')
    else:
        return os.system('clear')

cl()

user = input("Enter your name: ").upper()

def listgen():
   
    cl()

    todo = []

    try: 
        with open('mylist.txt', 'r') as f:
            todo = json.load(f)

    except:
        open('mylist.txt','w').close()

    print(f"Welcome to your To-do List, {user}!!\n")

    if todo==[]:
        print("There's nothing in your list yet!")
    else:
        print("Today we are doing:\n") 
        for i,task in enumerate(todo):
            print(f"{i+1}. {task}")

    print("\nOnce you have finished adding to your list, type 'finish'\nTo clear your list, just type 'clear'.")
    print("To exit, simply type 'exit'.\n\n")

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
            print(f"Thanks for coming, {user}! Press enter to close the window.")
            input()
            exit() 
        else:
            todo += [a]

    def betterclear(message):
        def clearscreen(func):
            def wrap():
                cl()
                print(f"---------  {message}  ---------\n")
                func()
            return wrap
        return clearscreen

    def rem():
            itemno = input("\n\nDo you want to remove an item? (type 'yes' or 'no'): ")
            if itemno.lower() == "yes":
                gone = int(input("Type the number of the item to be removed: ")) - 1
                try:
                    todo.pop(gone)
                except:
                    print("\nPick something from the list!")
                    rem()
                with open('mylist.txt', 'w') as f:
                    json.dump(todo, f)
                showlist()
            else:
                with open('mylist.txt', 'w') as f:
                    json.dump(todo, f)
                listgen()

    @betterclear(f"{user}'S LIST")
    def showlist():
        while("" in todo):
            todo.remove("")
        if todo == []:
            print("There's nothing in your list!")
            input("\nPress Enter to continue...")
            listgen()
        else:
            print("Today we will be doing:\n") 
            for i,task in enumerate(todo,1):
                print(f"{i}. {task}")
            rem()
        
        
    showlist()
listgen()
    


