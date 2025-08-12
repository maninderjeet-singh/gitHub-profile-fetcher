'''
# Day 2 — Functions, Loops & File Handling
    Goal: Be comfortable writing reusable code.
    
    Tasks:
    Write a function that:

        Takes a name & returns a greeting

        Writes that greeting to a text file

        Reads from the file and prints it
'''

def greeting(name):
    greetingTxt = f"Hello, {name}!"
    f = open('greeting.txt','a')
    f.write(greetingTxt+'\n')
    f.close()
    return greetingTxt

def readGreeting():
    with open('greeting.txt') as f:
        return f.read()


greeting('Maninderjeet Singh')
print(readGreeting())